from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.
class BaseModel(models.Model):
    # Using for all models
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    created_by = models.IntegerField(null=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)

    modified_by = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(default=None, null=True)
    deleted_by = models.IntegerField(null=True)

    class Meta:
        abstract = True
class AbstractBaseUser(AbstractUser):
    # Just using for User model
    # Not used password field of Abstract User
    password = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    created_by = models.IntegerField(null=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)

    modified_by = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(default=None, null=True)
    deleted_by = models.IntegerField(null=True)

    objects = UserManager()
    class Meta:
        abstract = True
