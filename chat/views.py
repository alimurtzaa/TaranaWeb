from django.shortcuts import get_object_or_404, redirect, render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import Http404, HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
@login_required
def chat_view(request, chatroom_name="demo-chat-group"):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()[:30]
    
    # other_user = User.objects.filter(groupmessage__group=chat_group
    # ).exclude(id=request.user.id).distinct().first()

    other_user = None
    if chat_group.is_private:
        if request.user not in chat_group.members.all():
            raise Http404()
        for member in chat_group.members.all():
            if member != request.user:
                other_user = member
                break

    form = ChatmessageCreateForm()
    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message' : message,
                'user' : request.user
            }
            return render(request, "chat/partials/chat_message_p.html", context)
    context = {
        'chat_messages':chat_messages,
        'form':form, 
        'other_user':other_user,
        'chatroom_name':chatroom_name,
        'chat_group':chat_group
    }

    return render(request, "chat/chat.html", context)

@login_required
def get_or_create_chatroom(request, username):
    if request.user.username == username:
        return redirect('chat')  #change to home
    
    other_user = User.objects.get(username=username)
    my_chatrooms = request.user.chat_groups.filter(is_private=True)

    if my_chatrooms.exists():
        for chatroom in my_chatrooms:
            if other_user in chatroom.members.all():
                return redirect('chatroom', chatroom.group_name)

    chatroom = ChatGroup.objects.create(is_private=True)
    chatroom.members.add(request.user, other_user)
    return redirect('chatroom', chatroom.group_name)

@login_required
def chat_file_upload(request, chatroom_name):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    if request.htmx and request.FILES:
        file = request.FILES['file']
        message = GroupMessage.objects.create(
            file = file,
            author = request.user,
            group = chat_group,
        )
        channel_layer = get_channel_layer()
        event = {
            'type':'message_handler',
            'message_id':message.id    
        }
        async_to_sync(channel_layer.group_send)(
            chatroom_name, event
        )
    return HttpResponse()

@login_required
def chatroom_leave_view(request, chatroom_name):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    if request.user not in chat_group.members.all():
        return Http404
    
    if request.method == "POST":
        chat_group.members.remove(request.user)
        return redirect('home')