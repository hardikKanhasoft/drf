# CRUD usin api decorators.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer
from apps.app2.models import Person
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from apps.accounts.models import CustomTokenBackend


@api_view(["GET", "POST", "PATCH", "PUT", "DELETE"])
@authentication_classes([CustomTokenBackend])
@permission_classes([IsAuthenticated])
def person_api(request):
    _id = request.query_params.get('id')  # Retrieve the 'id' from query parameter
    print("_id", _id)
    # import pdb;pdb.set_trace()
    if request.method == "GET":
        if _id:
            try:
                person = Person.objects.get(id=_id)  
                serializer = PersonSerializer(person)
                return Response({"Success":True, "data":serializer.data})
            except Person.DoesNotExist:
                return Response({"message": f"Details not found for id {_id}"})
        persons = Person.objects.all() 
        serializer = PersonSerializer(persons, many=True)
        return Response({"Success":True, "data":serializer.data})
    
    if request.method == "POST":
        print("request", request.data)
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success":True, "data":serializer.data})
        else:
            return Response(serializer.errors)
        
    if request.method == "PATCH":
        person = Person.objects.get(pk=_id)
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success":True,"data":serializer.data})
        else:
            return Response(serializer.errors)
    
    if request.method =="PUT":
        person = Person.objects.get(id=_id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success":True,"data":serializer.data})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        person = Person.objects.get(id=_id)
        person.delete()
        return Response({"Success":True,"msg": "Data Deleted"})

        
        

             
            
        
        
        





