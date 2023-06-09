# urls.py

from django.urls import path
from .views import person_api
urlpatterns = [
    path('person_api/', person_api, name='person_api'),
]