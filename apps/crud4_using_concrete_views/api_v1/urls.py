# urls.py

from django.urls import path
from .views import ListCreatePersonAPIView, RetrieveUpdateDestroyPersonAPIView
urlpatterns = [
    path('person_api/listcreateapiview/', ListCreatePersonAPIView.as_view(), name='person_api_listcreateapiview'),
    path('person_api/retrieveupdatedestroypersonapiview/<int:pk>/', RetrieveUpdateDestroyPersonAPIView.as_view(), name='PersonAPI'),
]