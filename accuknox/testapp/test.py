import threading
from django.db import transaction
from .models import CustomUser


def test_signals():
    print(f"Main thread ID: {threading.get_ident()}")

    print("\n>>> Testing Synchronous Execution")
    user1 = CustomUser.objects.create(username="test_sync")

    print("\n>>> Testing Same-Thread Execution")
    user2 = CustomUser.objects.create(username="test_thread")
    print("\n>>> Testing Transaction Behavior")
    with transaction.atomic():
        user3 = CustomUser.objects.create(username="test_transaction")
        print("User created but transaction not committed yet")

    print("Transaction committed")


test_signals()
