from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from users.serializers import CustomUserSerializer, SimpleUserSerializer


class AllUsersAPIView(ListAPIView):
    serializer_class = SimpleUserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]


class GetUserAPIView(RetrieveAPIView):
    serializer_class = SimpleUserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]