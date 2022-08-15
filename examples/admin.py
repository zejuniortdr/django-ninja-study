from django.contrib import admin

# Register your models here.
from .models import Example
from base.admin import BaseAdmin


class ExampleAdmin(BaseAdmin):
    model = Example


admin.site.register(Example, ExampleAdmin)
