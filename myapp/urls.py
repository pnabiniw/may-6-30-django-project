from django.urls import path
from .views import home, template_test, name_message
# from .views import home, template_test


urlpatterns = [
    path("template-test/", template_test, name="template_name"),
    path("user/<str:name>/", name_message, name='name_message'),
    path("", home, name='home'),  # "127.0.0.1:8000/myapp/home/"
]


# www.project.com/user/?search='jo'&name="Jonny"&page=10   # querystring or query params
