from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from api.serializers import StudentModelSerializer, StudentProfileModelSerializer
from myapp.models import Student


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()

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
