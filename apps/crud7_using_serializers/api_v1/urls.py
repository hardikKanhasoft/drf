# urls.py

from django.urls import path, include
from .views import PersonAPIViewSet

urlpatterns = [
    path('crud_serializer', PersonAPIViewSet.as_view(), name="crud_serializer"),
    path('crud_serializer/<int:pk>/', PersonAPIViewSet.as_view(), name="crud_serializer"),
    
]

