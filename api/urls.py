from django.urls import path
from .views import hello_api, InfoView, InfoListView, StudentView, StudentListView, \
    StudentAPIView, StudentListCreateAPIView


urlpatterns = [
    path("hello/", hello_api),
    path("info/", InfoView.as_view()),
    path("info-list/", InfoListView.as_view()),
    path("student/<int:id>/", StudentView.as_view()),
    path("student-view/<int:id>/", StudentAPIView.as_view()),
    path("student-list/", StudentListView.as_view()),
    path("student-list-create/", StudentListCreateAPIView.as_view()),
]
