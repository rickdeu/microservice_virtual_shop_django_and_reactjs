from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    name = models.CharField(
        max_length=200
    )
    image = models.ImageField(
        upload_to='categories/%Y/%m/%d',
        blank=True,
        default='shop.jpg'
        )


    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=200
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True,
        default='shop.jpg'
        )
    description = models.TextField(
        blank=True,
        null=True
        )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    is_available = models.BooleanField(
        default=True
        )

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['category']),
        ]
    def __str__(self):
        return self.name

