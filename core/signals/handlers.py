from django.dispatch import receiver
from store.signals import order_created

@receiver(order_created)
def on_order_created(sender, **kwargs):
    print(f"Order {kwargs['order']} has been created")