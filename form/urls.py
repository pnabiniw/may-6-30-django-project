from django.urls import path
from .views import template_form, student_detail, student_update, student_form, \
student_model_form, StudentCreateView, PortfolioView, StudentListView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("student-detail/<int:id>/", student_detail, name="student_detail"),
    path("student-update/<int:id>/", student_update, name="student_update"),
    path("student/", student_form, name="student_form"),
    path("student-model-form/", student_model_form, name="student_model_form"),
    path("student-create", StudentCreateView.as_view(), name="student_create"),
    path('portfolio/', login_required(PortfolioView.as_view())),
    path("student-list/", StudentListView.as_view()),
    path("", template_form, name="template_form")
]
