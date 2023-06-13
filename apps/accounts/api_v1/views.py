from rest_framework.viewsets import ModelViewSet
from apps.accounts.models import User
from apps.accounts.api_v1.serializers import UserSerializer
from rest_framework.response import Response

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = self.create_user(serializer)
            response = {"user" : UserSerializer(instance=user).data}
            return Response (response)
        
    def create_user(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data["password"])
        user.save()
        return user
    
    
    