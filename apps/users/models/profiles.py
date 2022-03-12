"""Profile user model."""

#Django
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


#User model
from apps.users.models import User



class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    avatar = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    """function to create a profile 
    for the user at the time it is created"""
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
