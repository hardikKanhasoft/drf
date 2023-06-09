# this views.py is allocated for accounts.

from rest_framework.views import APIView
from rest_framework.response import Response

class AddNumbersView(APIView):
    def post(self, request):
        num1 = int(request.data.get('num1'))
        num2 = int(request.data.get('num2'))
        result = num1 + num2
        return Response({'result': result})
