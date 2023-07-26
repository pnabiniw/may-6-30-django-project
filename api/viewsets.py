import requests
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.mixins import ListUpdateViewSet, CreateListUpdateViewSet
from api.serializers import StudentModelSerializer, StudentProfileModelSerializer, ClassRoomModelSerializer
from myapp.models import Student, ClassRoom
from .permissions import IsSuperUser


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'department', 'student_profile__email']
    filterset_fields = ["department", ]
    # permission_classes = [AllowAny, ]

    def get_permissions(self):
        # if self.action in ['list', 'retrieve']:
            # return [(IsSuperUser|IsAuthenticated)(), ]  # This is for Or
            # return [IsSuperUser(), IsAuthenticated(), ]  # This is for And
        # return [IsAuthenticated(), ]
        return [AllowAny(), ]

    def get_serializer_class(self):
        if self.action == "profile":
            return StudentProfileModelSerializer
        return StudentModelSerializer

    @action(detail=True)
    def profile(self, *args, **kwargs):
        student = self.get_object()
        try:
            profile = student.student_profile
        except:
            return Response({"detail": "No Profile"}, status=404)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)


class ClassRoomModelViewSet(CreateListUpdateViewSet):
    serializer_class = ClassRoomModelSerializer  # classroom list, classroom create, classroom delete,
    queryset = ClassRoom.objects.all()
    permission_classes = [AllowAny, ]

    @action(detail=True, url_path="all-students")
    def student(self, *args, **kwargs):
        classroom = self.get_object()
        students = Student.objects.filter(classroom=classroom)
        serializer = StudentModelSerializer(students, many=True)
        return Response(serializer.data)


# user/1/profile/
# classroom/1/student/
# list, create, update, retrieve, deslass Classtroy


# Use cases in FE
# response = axios.post("127.0.0.1:8000/api/login/", body={"username": "Jon", "password":"123"})
# localstorage.set(token, response.data['token'])
#
#
# token = localstorage.get("token")
# response = axios.post("127.0.0.1:8000/api/student/", body={"name": "Jon"}, headers={"Authorization": f"Token {token}"})
