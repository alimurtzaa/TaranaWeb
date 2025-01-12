from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        labels = {
            'title': 'Caption',
            'body': 'Tar'
        }
        widgets={
            'title': forms.TextInput(attrs={'placeholder':'Add title'}),
            'body': forms.Textarea(attrs={'rows':3, 'placeholder':'Write your tar here...', 'class':'font1 text-4xl'})
        }

class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows':3,'class':'font1 text-4xl'})
        }

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows':1, 'placeholder':'Add comment...','class':'mb-0'})
        }
        labels = {
            'body': ''
        }
