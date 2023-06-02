from django.urls import path
from .views import home, template_test, name_message, json_view, \
    inheritance_page1, inheritance_page2, portfolio
# from .views import home, template_test


urlpatterns = [
    path("template-test/", template_test, name="template_name"),
    path("user/<str:name>/", name_message, name='name_message'),
    path("json/", json_view, name="json_view"),
    path("inheritance-page1/", inheritance_page1, name="inheritance_page1"),
    path("inheritance-page2/", inheritance_page2, name="inheritance_page2"),
    path("", portfolio, name='portfolio'),  # "127.0.0.1:8000/myapp1/home/"
]


# www.project.com/user/?search='jo'&name="Jonny"&page=10   # querystring or query params
