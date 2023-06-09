from apps.app2.models import Person
from rest_framework.serializers import ModelSerializer

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        # fields = ["name", "city", "role"]
        fields = "__all__"