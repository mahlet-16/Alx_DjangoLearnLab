from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()  # Dynamically fetch the user model being used.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to automatically create a UserProfile
    whenever a new User instance is created.

    Args:
        sender: The model class (User).
        instance: The actual instance being saved.
        created: Boolean; True if a new instance was created, False otherwise.
        **kwargs: Additional keyword arguments.
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal handler to save the UserProfile whenever the
    associated User instance is updated.

    Args:
        sender: The model class (User).
        instance: The actual instance being saved.
        **kwargs: Additional keyword arguments.
    """
    # Access the related UserProfile and save it.
    instance.userprofiles.save()
