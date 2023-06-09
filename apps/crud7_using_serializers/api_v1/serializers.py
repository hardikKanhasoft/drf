from apps.app2.models import Person
from rest_framework import serializers  

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=24)
    role = serializers.CharField()

    def create(self, validated_data):
        print("-------------------- create serializer ------------------")
        instance = Person.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("-------------------- update serializer ------------------")
        instance.name = validated_data.get("name", instance.name)
        instance.city = validated_data.get("city", instance.city)
        instance.role = validated_data.get("role", instance.role)
        instance.save()
        return instance
    
# no delete method for the serializer