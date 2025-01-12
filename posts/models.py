from django.db import models
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='likedposts', through='LikePost')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering =['-created']

class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post.title}'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    likes = models.ManyToManyField(User, related_name='likedcomments', through='LikeComment')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} - {self.body[:30]}'
        except:
            return f'No Author - {self.body[:30]}'
        
    class Meta:
        ordering = ['-created']

class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.comment.body[:30]}'