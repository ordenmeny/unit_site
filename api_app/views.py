from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import *
from .models import *


class BaseViewApply:
    serializer_class = ApplySerializer
    queryset = Apply.objects.all()


class CreateApplyAPIView(BaseViewApply, ListCreateAPIView):
    pass




class BaseViewNews:
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class BaseViewEvents:
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class BaseViewProjects:
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()



class GetAllProjectsAPIView(BaseViewProjects, ListAPIView):
    pass


class GetProjectAPIView(BaseViewProjects, RetrieveAPIView):
    pass


class GetNewAPIView(BaseViewNews, RetrieveAPIView):
    pass


class GetAllNewsAPIView(BaseViewNews, ListAPIView):
    pass


class CreateEventAPIView(BaseViewEvents, ListCreateAPIView):
    pass


class GetEventAPIView(BaseViewEvents, RetrieveAPIView):
    pass


class UpdateOrDeleteEventAPIView(BaseViewEvents, RetrieveUpdateDestroyAPIView):
    pass
