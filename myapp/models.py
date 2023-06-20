from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE,
                                  related_name="classroom_students", null=True, blank=True)

    def __str__(self):
        return self.name
