from django.urls import path
from .views import hello_api, InfoView, InfoListView, StudentView, StudentListView


urlpatterns = [
    path("hello/", hello_api),
    path("info/", InfoView.as_view()),
    path("info-list/", InfoListView.as_view()),
    path("student/<int:id>/", StudentView.as_view()),
    path("student-list/", StudentListView.as_view()),
]
