from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]
        labels = {
            'full_name': 'Name',
            'location': 'City',
        }
        widgets = {
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows':3, 'placeholder':'Tell us about yourself'}),
            'full_name': forms.TextInput(attrs={'placeholder':'Name'}),
            'location': forms.TextInput(attrs={'placeholder':'Location'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
        }
