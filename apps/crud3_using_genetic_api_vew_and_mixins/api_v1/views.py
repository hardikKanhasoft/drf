# # CRUD usin GenericAPIView and mixins.

from apps.app2.api_v1.serializers import PersonSerializer
from apps.app2.models import Person
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from apps.accounts.models import CustomTokenBackend

# List and Create - PK Not Required
class ListCreatePersonAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [CustomTokenBackend]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):       
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# retrieve, put and delete - PK Required
class ReadUpdateDeletePersonAPI(
    GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [CustomTokenBackend]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)