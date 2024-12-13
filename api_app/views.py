from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import EventSerializer
from .models import Event


class BaseViewEvents:
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class CreateEventAPIView(BaseViewEvents, ListCreateAPIView):
    pass


class GetEventAPIView(BaseViewEvents, RetrieveAPIView):
    pass


class UpdateOrDeleteEventAPIView(BaseViewEvents, RetrieveUpdateDestroyAPIView):
    pass

