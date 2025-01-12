from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import get_object_or_404

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if not user.is_superuser:
        if created:
            Profile.objects.create(user=user, email=user.email)
        else:
            profile = Profile.objects.get(user=user)
            profile.email = user.email
            profile.save()
        
 
@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    if not created:
        user = get_object_or_404(User, id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()
