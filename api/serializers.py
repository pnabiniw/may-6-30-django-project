from rest_framework import serializers
from myapp.models import Student, ClassRoom, StudentProfile


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


class StudentProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        # fields = "__all__"
        fields = ['email', 'address', 'phone']


class StudentModelSerializer(serializers.ModelSerializer):
    about_me = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ["id", "name", "age", "department", "classroom",
                  "about_me", "profile"]  # '__all__'

    def get_profile(self, obj):
        try:
            profile = obj.student_profile
        except:
            profile = None
        return StudentProfileModelSerializer(profile).data
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
        # if request and request.method == "GET":
        #     self.Meta.depth = 1
        if request and request.method.lower() == 'post':
            fields['profile'] = StudentProfileModelSerializer()
        return fields

    def create(self, validated_data):
        profile = validated_data.pop("profile")  # {"phone": "9890989098", "} phone="9890-980",
        instance = super().create(validated_data)
        StudentProfile.objects.create(student=instance, **profile)
        instance.profile = profile
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request and request.method.lower() == 'post':
            if instance.classroom is not None:
                data['classroom'] = ClassRoomModelSerializer(instance.classroom).data
        return data

    # def update(self, instance, validated_data):
    #     instance.name =  validated_data["name"]
    #     instance.save()
    #     return super().update(instance, validated_data)
