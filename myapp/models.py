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


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, 
    on_delete=models.CASCADE, related_name="student_profile")   # related_name is model name by default for
    # One-One relation
    email = models.EmailField()
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    profile_picture = models.FileField(upload_to="profile_picture", null=True, blank=True)

    def __str__(self):  # __str__
        return f"profile of {self.student.name}"


class Publication(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication, 
    related_name="publiction_articles")

    def __str__(self):
        return self.headline


class ArticlePublication(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    xyz = models.CharField