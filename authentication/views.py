from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from authentication.models import Student
from authentication.serializers import StudentProfileUpdateSerializer


# Create your views here.
@extend_schema(tags=['Student'], request=StudentProfileUpdateSerializer, responses=StudentProfileUpdateSerializer)
class StudentUpdateApiView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentProfileUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user



