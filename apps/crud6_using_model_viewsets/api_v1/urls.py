# urls.py

from django.urls import path, include
from .views import PersonModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("personmodelviewset", PersonModelViewSet, basename="personviewset")

urlpatterns = [
    path("", include(router.urls)),
]

