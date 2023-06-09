# urls.py

from django.urls import path
from apps.app1.api_v1.views import AddNumbersView

urlpatterns = [
    path('add/', AddNumbersView.as_view(), name='add-numbers'),
    # curl --location 'http://127.0.0.1:8000/api/v1/app1/add/' \
    # --header 'Content-Type: application/json' \
    # --data '{"num1": 3, "num2": 4}'
    
]
