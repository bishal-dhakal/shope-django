from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver
from .models import CustomUser
 
@receiver(post_save, sender=CustomUser)
def new_user_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New user '{instance.username}' has been added!")