from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.crypto import get_random_string
from .models import User

@receiver(post_save, sender=User)
def create_authentication_token(sender, instance, created, **kwargs):
    if created and not instance.authentication_token:
        # Generate a unique authentication token
        instance.authentication_token = get_random_string(length=16)
        instance.save()