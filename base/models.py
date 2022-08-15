from django.db import models
from django.utils.timezone import now

# Create your models here.
from .fields import UUIDPrimaryKeyField
from .managers import SoftAliveManager, SoftDeletedManager

class BaseModel(models.Model):
    id = UUIDPrimaryKeyField()
    deleted_at = models.DateTimeField(blank=True, null=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SoftAliveManager()
    deleted = SoftDeletedManager()

    class Meta:
        abstract = True


    def __str__(self):
        return f'{self.id}'

    def delete(self, *args, **kwargs):
        self.deleted_at = now()
        self.save(update_fields=("deleted_at",))
        return 1, {self._meta.label: 1}

    def undelete(self):
        self.deleted_at = None
        self.save(update_fields=("deleted_at",))
        return 1, {self._meta.label: 1}

    def to_dict(self, fields=None):
        fields = fields.split(',') if fields else []
        response = self.__dict__
        response.pop("_state")
        if not fields:
            return response

        return {
            k: response.get(k) for k in fields
        }
