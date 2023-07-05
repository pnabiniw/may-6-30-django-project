from django.urls import path
from .views import user_login, user_logout


urlpatterns = [
    path("logout/", user_logout, name='logout'),
    path("", user_login, name="login")
]
