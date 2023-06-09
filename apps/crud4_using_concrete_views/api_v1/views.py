# # CRUD usin GenericAPIView and mixins.
from apps.app2.models import Person
from apps.app2.api_v1.serializers import PersonSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

class ListCreatePersonAPIView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class RetrieveUpdateDestroyPersonAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    
    