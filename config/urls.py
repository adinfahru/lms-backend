from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('classes.urls')),
    path('api/users/', include('users.urls')),
    path('api/classes/', include('classes.urls')),
]