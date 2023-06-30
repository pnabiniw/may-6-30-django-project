from django.urls import path
from .views import template_form, student_detail, student_update


urlpatterns = [
    path("student-detail/<int:id>/", student_detail, name="student_detail"),
    path("student-update/<int:id>/", student_update, name="student_update"),
    path("", template_form, name="template_form")
]
