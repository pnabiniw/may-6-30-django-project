from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer, StudentModelSerializer

from myapp.models import Student


"""
------------API Introduction ---------------------
=> API stands for Application Programmable Interface
=> APIs are the services provided by third parties.
=> Here, we are building our own APIs
=> APIs and SDK are sometimes used interchangeably
=> Here we build Restful APIs
=> DRF (Django RestFramework) is the library built on top of django to create Restful APIs

-------------What are RestFul APIs?-------------------
=> Rest stands for Representational State Transfer.
=> Restful APIs are one of the ways to communicate among multiple services.
=> In Restful APIs, we communication between services using JSON data format.
"""


def hello_api(request):
    return JsonResponse({
        "message": "Hello World"
    })


class InfoView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "id": 1,
            "name": "Alex",
            "age": 23,
            "dept": "IT"
        })


class InfoListView(APIView):
    def get(self, *args, **kwargs):
        return Response([
            {"id": 1, "name": "Jon", "age": 31},
            {"id": 2, "name": "Jane", "age": 25}
        ])


class StudentView(APIView):
    def get(self, *args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs['id'])
        except Student.DoesNotExist:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        response = {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "department": student.department,
            "classroom": student.classroom.name if student.classroom else None
        }
        return Response(response)


class StudentListView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        response = [dict(name=student.name, age=student.age, department=student.department) for student in students]
        return Response(response)


class StudentAPIView(APIView):
    def get(self, *args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs['id'])
        except Student.DoesNotExist:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentModelSerializer(student)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        serializer = StudentModelSerializer(data=self.request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            age = serializer.validated_data.get("age")
            department = serializer.validated_data.get("department")
            classroom = serializer.validated_data.get("classroom")
            Student.objects.create(name=name, age=age, department=department,
                                   classroom=classroom)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentListCreateAPIView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True, context={"request": self.request})
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        serializer = StudentModelSerializer(data=self.request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
