from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Count
from django.core.paginator import Paginator
from .models import *
from.forms import *

def home_view(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 3)
    page = int(request.GET.get('page', 1))
    try:
        posts = paginator.page(page)
    except:
        return HttpResponse('')

    context={
        'posts': posts,
        'page': page
    }

    if request.htmx:
        return render(request, 'snippets/loop_home_posts.html', context)

    return render(request, 'posts/home.html', context)

@login_required
def create_post_view(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect ('home')

    return render(request, 'posts/create_post.html', {'form': form})

@login_required
def delete_post_view(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect ('home')
    return render(request, 'posts/delete_post.html', {'post': post})

@login_required
def edit_post_view(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    form = PostEditForm(instance=post)
    if request.method =='POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect ('home')
    return render(request, 'posts/edit_post.html', {'post': post, 'form': form})

def post_page_view(request, id):
    post = get_object_or_404(Post, id=id)
    commentform = CommentCreateForm()

    # Check if the request is a request from HTMX
    # if request.META.get('HTTP_HX_REQUEST')  => This is the same as the line below as we have installed django-htmx

    if request.htmx:
        if 'top' in request.GET:
            # comments = post.comments.filter(likes__isnull=False).distinct()
            comments = post.comments.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by("-num_likes")
        else:
            comments = post.comments.all()
        return render(request, 'snippets/loop_postpage_comments.html', {'comments': comments})


    context = {
        'post': post,
        'commentform': commentform,
    } 
    return render(request, 'posts/post_page.html', context)

@login_required
def comment_sent(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()
            
    return render(request, 'snippets/add_comment.html', {'comment': comment, 'post': post})


@login_required
def delete_comment_view(request, id):
    comment = get_object_or_404(Comment, id=id, author=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect ('post', comment.parent_post.id)
    return render(request, 'posts/delete_comment.html', {'comment': comment})


# Like Toggle Decorator
def like_toggle(model):
    def inner_func(func):
        def wrapper(request, *args, **kwargs):
            instance = get_object_or_404(model, id=kwargs['id'])
            if instance.author != request.user:
                like_exist = instance.likes.filter(username=request.user.username).exists()
                if like_exist:
                    instance.likes.remove(request.user)
                else:
                    instance.likes.add(request.user)
            return func(request, instance)
        return wrapper
    return inner_func

@login_required
@like_toggle(Post)
def like_post(request, post):
    return render(request, 'snippets/likes.html', {'post': post})

@login_required
@like_toggle(Comment)
def like_comment(request, comment):
    return render(request, 'snippets/likes_comment.html', {'comment': comment})

