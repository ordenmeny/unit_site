from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from users.serializers import CustomUserSerializer


class AllUsersAPIView(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = get_user_model().objects.all()
    # allow all users:
    permission_classes = [AllowAny]
