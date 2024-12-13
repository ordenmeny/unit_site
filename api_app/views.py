from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import EventSerializer
from .models import Event


class CreateEventAPIView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class GetEventAPIView(RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class UpdateOrDeleteEventAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
