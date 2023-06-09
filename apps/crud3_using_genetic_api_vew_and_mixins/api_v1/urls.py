# urls.py

from django.urls import path
from .views import ListCreatePersonAPI, ReadUpdateDeletePersonAPI
urlpatterns = [
    path('person_api/', ListCreatePersonAPI.as_view(), name='PersonAPI'),
    path('person_api/mixin/<int:pk>/', ReadUpdateDeletePersonAPI.as_view(), name='PersonAPI'),
]

