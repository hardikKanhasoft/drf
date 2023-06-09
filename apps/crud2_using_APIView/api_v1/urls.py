# urls.py

from django.urls import path
from .views import PersonAPIView
urlpatterns = [
    path('person_api/', PersonAPIView.as_view(), name='PersonAPI'),
]