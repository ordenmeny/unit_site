from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

# url-prefix: api-app/

urlpatterns = [
    path('create-event/', CreateEventAPIView.as_view(), name='create-event'),  # POST
    path('all-events/', CreateEventAPIView.as_view(), name='all-events'),  # GET
    path('get-event/<int:pk>/', GetEventAPIView.as_view(), name='get-event'),  # GET
    path('upd-del-event/<int:pk>/', UpdateOrDeleteEventAPIView.as_view(), name='update-delete-event'),  # PATCH
]


# POST: create-event/ - создание события (для админов)
# GET: all-events/ - вывод всех событий (для всех)
# GET: get-event/<int:pk>/ - получение события (для всех)
# PATCH: upd-del-event/<int:pk>/ - изменение события (для админов)