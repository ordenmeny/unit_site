from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import CustomUser
from django.contrib import admin


class CustomUserAdmin(admin.ModelAdmin):
    exclude = (
        'password', 'email', 'groups', 'user_permissions', 'is_active', 'is_staff', 'is_superuser', 'date_joined',
        'last_login', "username")


admin.site.register(get_user_model(), CustomUserAdmin)
