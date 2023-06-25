from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include('form.urls')),
    path("", include("myapp.urls"))
]


# Convention to follow urls creation
# Use hyphens
# Keep it short and informative  (www.project.com/user/id/profile)
# AVoid using ids in the urld   user/admin/profile/
# For pagination don't do www.project.com/user/page-1/   Do: www.project.com/user/?page=1
