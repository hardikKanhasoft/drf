# # CRUD usin GenericAPIView and mixins.
from apps.app2.models import Person
from apps.app2.api_v1.serializers import PersonSerializer
from rest_framework.viewsets import ModelViewSet
    
class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer