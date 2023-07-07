from rest_framework import serializers
from myapp.models import Student, ClassRoom


class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=5)
    age = serializers.IntegerField()
    department = serializers.CharField()
    classroom = ClassRoomSerializer()


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "age", "department", "classroom"]  # '__all__'

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "GET":
            fields['classroom'] = ClassRoomModelSerializer()
        return fields
