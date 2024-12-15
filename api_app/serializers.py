from rest_framework.serializers import ModelSerializer
from .models import *


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"