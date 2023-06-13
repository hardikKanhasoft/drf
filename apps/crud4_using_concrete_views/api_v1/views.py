# # CRUD usin GenericAPIView and mixins.
from apps.app2.models import Person
from apps.app2.api_v1.serializers import PersonSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from apps.accounts.models import CustomTokenBackend

class ListCreatePersonAPIView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [CustomTokenBackend]
    permission_classes = [IsAuthenticated]
    
class RetrieveUpdateDestroyPersonAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [CustomTokenBackend]
    permission_classes = [IsAuthenticated]
    
    
    