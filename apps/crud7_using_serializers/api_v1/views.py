from apps.app2.models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer
    
class PersonAPIViewSet(APIView):      
    def get(self, request, pk=None, format=None):
        _id = pk
        if _id:
            person = Person.objects.get(id=_id)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # import pdb;pdb.set_trace()
        serializer = PersonSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg": "Data Created", "data":serializer.data})
        return Response(serializer.errors)
    
    def patch(self, request, pk=None):
        _id=pk
        person = Person.objects.get(id=_id)
        serializer = PersonSerializer(person,data = request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg": "Data Created", "data":serializer.data})
        return Response(serializer.errors)