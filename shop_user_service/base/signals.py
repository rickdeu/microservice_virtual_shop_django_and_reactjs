
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from shop.models import Customer

@receiver(post_save, sender=User)
def signup_signal(sender, instance, **kwargs):
    # Create a new customer if the user is created
    first_name = instance.get_full_name() or instance.username
    email = instance.email
    Customer.objects.update_or_create(
        name=first_name,
        email=email,
        user=instance
    )
    print('Customer created!')