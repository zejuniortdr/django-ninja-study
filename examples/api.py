from django.shortcuts import  get_object_or_404
import uuid

from ninja import Router
from ninja.security import django_auth

from .models import Example
from .schema import ExampleSchema

router = Router()


@router.get("/",  tags=[__name__])
def getlist(request):
    examples = Example.objects.all()
    return {
        "count": examples.count(),
        "objects": [
            example.to_dict(fields=request.GET.get("fields"))
            for example in examples
        ],
    }


@router.get("/{id}/",  tags=[__name__])
def detail(request, id:uuid.UUID):
    example = get_object_or_404(Example, id=id)
    return example.to_dict(fields=request.GET.get("fields"))


@router.post("/", response=ExampleSchema,  tags=[__name__])
def add(request, example: ExampleSchema):
    example = Example(**example.dict())
    example.save()
    return example


@router.patch("/{id}/", response=ExampleSchema, tags=[__name__])
def update(request, id:uuid.UUID, example_schema: ExampleSchema):
    example = get_object_or_404(Example, id=id)
    example.name = example_schema.name
    example.save()
    return example

@router.delete("/{id}/",  tags=[__name__])
def delete(request, id:uuid.UUID, example_schema: ExampleSchema):
    example = get_object_or_404(Example, id=id)
    example.delete()
    return {}
