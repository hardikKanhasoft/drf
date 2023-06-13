# # CRUD usin GenericAPIView and mixins.
from apps.app2.models import Person
from rest_framework import status
from apps.app2.api_v1.serializers import PersonSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.accounts.models import CustomTokenBackend


class PersonViewset(ViewSet):
    authentication_classes = [CustomTokenBackend]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        _id = pk
        if _id:
            person = Person.objects.get(id=_id)
            serializer = PersonSerializer(person)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def update(self, request, pk):
        _id = pk
        stu = Person.objects.get(pk=_id)
        serializer = PersonSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Complete Data Updated","data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        _id = pk
        stu = Person.objects.get(pk=_id)
        serializer = PersonSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Complete Data Updated","data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        _id = pk
        stu = Person.objects.get(pk=_id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
