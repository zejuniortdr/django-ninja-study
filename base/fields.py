import uuid

from django.db import models


class UUIDPrimaryKeyField(models.UUIDField):
    """
    UUIDField that defaults to UUID4 and being a Primary Key of any model
    """

    def __init__(self, *args, **kwargs):
        kwargs["primary_key"] = True
        kwargs["editable"] = False
        kwargs["default"] = uuid.uuid4
        super().__init__(*args, **kwargs)
