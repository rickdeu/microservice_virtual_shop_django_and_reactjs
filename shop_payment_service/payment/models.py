from django.db import models
from .base import BaseModel

class PaymentMethod(BaseModel):
    """PaymentMethod Model"""

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    class Meta:
        """Meta"""

        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        """Model Name"""
        return str(self.name)


class Payment(BaseModel):
    """ "PaymentMethod Model"""

    order = models.CharField(max_length=100, verbose_name='Order')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)
    currency = models.CharField(max_length=200)

    class Meta:

        ordering = ["created_at"]
        indexes = [models.Index(fields=["payment_method"])]

    def __str__(self):
        """Model Name"""
        return str(self.pk)