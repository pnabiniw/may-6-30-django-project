from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, \
    RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from myapp.models import Student
from .serializers import StudentModelSerializer


class StudentListGenericView(ListAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    def get_serializer_context(self):
        return {
            "request": self.request
        }


class StudentCreateGenericView(CreateAPIView):
    serializer_class = StudentModelSerializer
    # queryset = Student.objects.all()


class StudentListCreateGenericView(ListCreateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['title'] = "Student List Create"
        return context


class StudentRetrieveGenericView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentUpdateGenericView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentDeleteGenericView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentRetrieveUpdateDeleteGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentModelSerializer

    def get_queryset(self):
        print(self.request)
        print(self.request.path)
        return Student.objects.filter(department="IT")

    # def get_permissions(self):
    #     pass
    #
    # def get_serializer_class(self):
    #     pass
    #
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass


"""
Views that can be grouped together
=> List and Create
=> Retrieve, Update, Destroy

"""

# classroom, created =  ClassRoom.objects.get_or_create(name="One")
# student, created = Student.objects.update_or_create(email="a@a.com", defaults={"name": "Jon", "age": 23})