from django.db import models
from .base import BaseModel


class Payment(BaseModel):
    """ "PaymentMethod"""

    order = models.CharField(max_length=100, verbose_name='Order')
    user = models.CharField(max_length=100, verbose_name='User')
    payment_method = models.CharField(max_length=100, default='STRIP', verbose_name='Payment Method')
    payment_status = models.BooleanField(default=False, verbose_name='Is Paid ?')
    amount = models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Amount')
    currency = models.CharField(max_length=200, default='USD')

    """card information"""
    card_number = models.CharField(max_length=150)
    expiry_month = models.CharField(max_length=150)
    expiry_year = models.CharField(max_length=150)
    cvc = models.CharField(max_length=150)

    class Meta:
        ordering = ["created_at"]
        unique_together = (('order', 'payment_status'),)
        indexes = [models.Index(fields=["payment_method"])]

    def __str__(self):
        return self.amount
