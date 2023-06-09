# CRUD usin api decorators.

from rest_framework.response import Response
from .serializers import PersonSerializer
from apps.app2.models import Person
from rest_framework.views import APIView
from rest_framework import status


class PersonAPIView(APIView):
    def get(self, request, *args, **kwargs):
        _id = request.query_params.get('id')  # Retrieve the 'id' from query parameter
        if _id:
            try:
                person = Person.objects.get(id=_id)  
                serializer = PersonSerializer(person)
                return Response({"Success":True, "data":serializer.data})
            except Person.DoesNotExist:
                return Response({"message": f"Details not found for id {_id}"})
        person = Person.objects.all()
        serializer = PersonSerializer(person, many= True)
        return Response({"Success":True, "data":serializer.data})
        
    def post(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success":True, "data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        _id = request.query_params.get('id')
        person = Person.objects.get(id=_id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success":True, "data":serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request):
        _id = request.query_params.get('id')
        person = Person.objects.get(id=_id)
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success":True, "data":serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        _id = request.query_params.get('id')
        person = Person.objects.get(id=_id)
        person.delete()
        return Response({"Success":True,"msg": "Data Deleted"})

            

            
        
        
        
        
        





