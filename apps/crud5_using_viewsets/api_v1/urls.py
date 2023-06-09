# urls.py

from django.urls import path, include
from .views import PersonViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("personviewset", PersonViewset, basename="personviewset")

urlpatterns = [
    path("", include(router.urls)),
    # path('personviewset/', PersonViewset, basename="personviewset"),
    # path('person_api/retrieveupdatedestroypersonapiview/<int:pk>/', RetrieveUpdateDestroyPersonAPIView.as_view(), name='PersonAPI'),
]

