from django.urls import path
from .views import hello_api, InfoView, InfoListView, StudentView, StudentListView, \
    StudentAPIView, StudentListCreateAPIView
from .generic_views import StudentListGenericView, StudentCreateGenericView, StudentListCreateGenericView, \
    StudentRetrieveGenericView, StudentUpdateGenericView, StudentDeleteGenericView, StudentRetrieveUpdateDeleteGenericView

urlpatterns = [
    path("hello/", hello_api),
    path("info/", InfoView.as_view()),
    path("info-list/", InfoListView.as_view()),
    path("student/<int:id>/", StudentView.as_view()),
    path("student-view/<int:id>/", StudentAPIView.as_view()),
    path("student-list/", StudentListView.as_view()),
    path("student-list-create/", StudentListCreateAPIView.as_view()),

    # Generic Views
    path("student-list-generic/", StudentListGenericView.as_view()),
    path("student-create-generic/", StudentCreateGenericView.as_view()),
    path("student-list-create-generic/", StudentListCreateGenericView.as_view()),
    path("student-retrieve-generic/<int:pk>/", StudentRetrieveGenericView.as_view()),
    path("student-update-generic/<int:pk>/", StudentUpdateGenericView.as_view()),
    path("student-delete-generic/<int:pk>/", StudentDeleteGenericView.as_view()),
    path("student-retrieve-update-delete-generic/<int:pk>/", StudentRetrieveUpdateDeleteGenericView.as_view()),
]
