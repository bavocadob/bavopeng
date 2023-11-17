from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('됨?')
        Profile.objects.create(user=instance, nickname=instance.username)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print('됨?22')
    instance.profile.save()
