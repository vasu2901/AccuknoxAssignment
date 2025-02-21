import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def sync_signal_handler(sender, instance, **kwargs):
    print("Sync Signal handler started")
    time.sleep(3)
    print("Sync Signal handler finished")


@receiver(post_save, sender=CustomUser)
def thread_signal_handler(sender, instance, **kwargs):
    print(f"Thread Signal handler running in thread: {threading.get_ident()}")


@receiver(post_save, sender=CustomUser)
def transaction_signal_handler(sender, instance, **kwargs):
    print("Transaction Signal received.")
    print(
        f"User exists in DB: {CustomUser.objects.filter(username=instance.username).exists()}"
    )
