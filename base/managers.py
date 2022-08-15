from django.db.models import QuerySet, manager
from django.utils import timezone


class SoftAliveQuerySet(QuerySet):
    def delete(self):
        """
        Overrides QuerySet.delete to soft delete instead.
        """
        rows = self.update(deleted_at=timezone.now())
        return rows, {self.model._meta.label: rows}


class SoftAliveManager(manager.BaseManager.from_queryset(SoftAliveQuerySet)):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeletedManager(manager.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=False)
