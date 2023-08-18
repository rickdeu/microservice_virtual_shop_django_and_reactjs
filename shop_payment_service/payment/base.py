from django.db import models

class BaseModel(models.Model):
    # Using for all models
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)

    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    modified_by = models.IntegerField(null=True, blank=True)

    is_deleted = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(default=None, null=True)
    deleted_by = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
