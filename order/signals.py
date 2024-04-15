from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import Order, OrderItem


@receiver(post_save, sender=OrderItem)
def new_user_saved(sender, instance, created, **kwargs):
    if created:
        pass
