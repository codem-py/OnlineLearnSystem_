from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from authentication.models import Student


class StudentProfileUpdateSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['image', 'password']

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.password = make_password(validated_data.pop('password'))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

