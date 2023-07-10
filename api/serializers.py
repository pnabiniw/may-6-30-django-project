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
    about_me = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ["id", "name", "age", "department", "classroom", "about_me"]  # '__all__'

    @staticmethod
    def get_about_me(student):
        return f"Hello I'm {student.name} and I'm {student.age} years old"

    def validate(self, attrs):
        if attrs["name"] == "Jon" or attrs["age"] > 50:
            raise serializers.ValidationError("Name can;t be Jon or age can't be more that 50")
        return attrs

    def validate_department(self, department):
        request = self.context.get('request')
        if request and request.method.lower() == 'post':
            if department == "IT":
                raise serializers.ValidationError("Department cant be IT")
        return department

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        print(self.context)
        if request and request.method == "GET":
            fields['classroom'] = ClassRoomModelSerializer()
        return fields
