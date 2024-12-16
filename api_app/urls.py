from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

# url-prefix: api-app/

urlpatterns = [
    path('all-events/', CreateEventAPIView.as_view()),  # GET
    path('get-event/<int:pk>/', GetEventAPIView.as_view()),  # GET
    path('all-news/', GetAllNewsAPIView.as_view()),  # GET
    path('get-new/<int:pk>/', GetNewAPIView.as_view()),  # GET
    path('all-projects/', GetAllProjectsAPIView.as_view()),
    path('get-project/<int:pk>/', GetProjectAPIView.as_view()),

    path('create-event/', CreateEventAPIView.as_view()),  # POST, GET

    path('create-apply/', CreateApplyAPIView.as_view()),  # POST, GET(all)
]

# GET: all-events/ - вывод всех событий
# GET: get-event/<int:pk>/ - получение события
# GET: all-news/ - вывод всех новостей
# GET: get-new/<int:pk>/ - получение конкретной новости
