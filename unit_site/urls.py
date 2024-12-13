from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('users.urls')),
    path('api-app/', include('api_app.urls')),
]