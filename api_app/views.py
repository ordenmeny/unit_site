from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import *
from .models import *
import telebot


TOKEN = "7776430508:AAFrx_63g1wJjM9hiyXqxM90KCX1E81heyA"
CHAT_ID = [1692072411, ]  # user_id админа. 1206446127

tb = telebot.TeleBot(TOKEN)


class BaseViewApply:
    serializer_class = ApplySerializer
    queryset = Apply.objects.all()


class BaseViewNews:
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class BaseViewEvents:
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class BaseViewProjects:
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class CreateNewAPIView(BaseViewNews, ListCreateAPIView):
    pass
    #     def post(self, request, *args, **kwargs):
    #         return self.create(request, *args, **kwargs)


class CreateApplyAPIView(BaseViewApply, ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        for user_id in CHAT_ID:
            text = f"Пришла заявка на участие в ЮНИТ. ФИО: {request.data['name']}"
            tb.send_message(user_id, text)

        return self.create(request, *args, **kwargs)


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
