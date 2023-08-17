from django.db import models
from base.models import BaseModel
from django.conf import settings

class Customer(BaseModel):
    """Customer Model"""

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    picture = models.ImageField(upload_to="profile/images")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        """Meta"""
 
        ordering = ["first_name", 'last_name']
        indexes = [models.Index(fields=["user", 'email', 'phone'])]

    def __str__(self):
        """Module name"""
        return f'{self.first_name} {self.last_name}'