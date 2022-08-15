import uuid

from django.urls import path

from .api import router
from base.api import api


api.add_router("/v1/", router)

urlpatterns = [
    path("v1/", api.urls),
]
