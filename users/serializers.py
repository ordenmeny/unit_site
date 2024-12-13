from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = '__all__'
