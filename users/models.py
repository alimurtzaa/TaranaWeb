from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from django_resized import ResizedImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20, blank=True, null=True)
    image = ResizedImageField(size=[600, 600], quality=85,  upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField( blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
    @property
    def avatar(self):
        try:
            avatar =  self.image.url
        except:
            avatar = static('images/avatar_default.svg')
        return avatar
    
    @property
    def name(self):
        if self.full_name:
            name = self.full_name
        else:
            name = self.user.username
        return name