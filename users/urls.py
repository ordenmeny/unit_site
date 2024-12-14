from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path("all-users/", AllUsersAPIView.as_view()),
    path("get-user/<int:pk>/", GetUserAPIView.as_view()),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
# GET: all-users/ - вывод всех пользователей
