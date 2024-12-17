from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = '__all__'


class SimpleUserSerializer(UserSerializer):
    class Meta(CustomUserSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'social_link', 'description', 'position', 'image')
