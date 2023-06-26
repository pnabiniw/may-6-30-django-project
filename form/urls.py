from django.urls import path
from .views import template_form, student_detail


urlpatterns = [
    path("student-detail/<int:id>/", student_detail, name="student_detail"),
    path("", template_form, name="template_form")
]
