from django.db import models

# Create your models here.

from base.models import BaseModel
from django.forms.models import model_to_dict



class Example(BaseModel):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
