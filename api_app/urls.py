from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

# url-prefix: api-app/

urlpatterns = [
    path('all-events/', CreateEventAPIView.as_view(), name='all_events'),  # GET
    path('get-event/<int:pk>/', GetEventAPIView.as_view(), name='get_event'),  # GET
    path('all-news/', GetAllNewsAPIView.as_view(), name='all_news'),  # GET
    path('get-new/<int:pk>/', GetNewAPIView.as_view(), name='get_new'),  # GET
]


# GET: all-events/ - вывод всех событий
# GET: get-event/<int:pk>/ - получение события
# GET: all-news/ - вывод всех новостей
# GET: get-new/<int:pk>/ - получение конкретной новости

