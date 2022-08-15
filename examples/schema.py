from ninja import ModelSchema
from ninja.orm import create_schema

from .models import Example


ExampleSchema = create_schema(Example)
