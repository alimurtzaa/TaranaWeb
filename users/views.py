from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models import Count, Q
from .forms import ProfileForm
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from allauth.account.utils import send_email_confirmation

def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
    posts = profile.user.posts.all()

    if request.htmx:
        if 'topposts' in request.GET:
            posts = posts.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by('-num_likes')
        elif 'topcomments' in request.GET:
            comments = profile.user.comments.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by('-num_likes')
            return render(request, 'snippets/loop_profile_comments.html', {'comments': comments})
        elif 'likedposts' in request.GET:
            posts = profile.user.likedposts.order_by('-likepost__created')
        return render(request, 'snippets/loop_profile_posts.html', {'posts': posts})


    context= {
        "profile": profile,
        "posts": posts,
        } 
        
    
    return render(request, 'users/profile.html', context)

@login_required
def profile_edit_view(request):
    form = ProfileForm(instance = request.user.profile)
    account_verified = False
    if request.user.emailaddress_set.exists():
        if request.user.emailaddress_set.get(primary=True).verified:
            account_verified = True
    elif not request.user.emailaddress_set.exists(): 
        account_verified = True
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid:
            form.save()
            if request.user.emailaddress_set.get(primary=True).verified:
                return redirect('profile')
            else:
                return redirect('profile-verify-email')
    
    if request.path == reverse('profile-onboarding'):
        return render(request, 'users/profile_onboarding.html', {"form":form})
    else:
        return render(request, 'users/profile_edit.html', {"form":form, 'account_verified':account_verified})

@login_required
def profile_delete_view(request):
    user = request.user
    if request.method=="POST":
        logout(request)
        user.delete()
        return redirect('home')
    return render(request, 'users/profile_delete.html')

@login_required
def search(request):
    return render(request, 'users/search_users.html')

@login_required
def list_search_users(request):
    letters = request.GET.get('search_user')
    if request.htmx:
        if len(letters) > 0:
            profiles = Profile.objects.filter(full_name__icontains = letters)
            users_id = profiles.values_list('user', flat=True)

            users = User.objects.filter(
                Q(username__icontains=letters) | Q(id__in = users_id)
            ).exclude(username=request.user.username)
            return render(request, 'users/list_searchusers.html', {'users':users})
        else:
            return HttpResponse('')
    else:
        raise Http404()
    
def profile_verify_email(request):
    send_email_confirmation(request, request.user)
    return redirect('profile')