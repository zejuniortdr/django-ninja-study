from django.contrib import admin

# Register your models here.
from .models import BaseModel

class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', 'created_at', 'updated_at',)
    model = BaseModel
