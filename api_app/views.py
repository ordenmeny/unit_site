from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import *
from .models import *


class GetNewAPIView(RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class GetAllNewsAPIView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class BaseViewEvents:
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class CreateEventAPIView(BaseViewEvents, ListCreateAPIView):
    pass


class GetEventAPIView(BaseViewEvents, RetrieveAPIView):
    pass


class UpdateOrDeleteEventAPIView(BaseViewEvents, RetrieveUpdateDestroyAPIView):
    pass
