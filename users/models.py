from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    social_link = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=512, blank=True, null=True)

    # photo = models.ImageField(upload_to='user_photos/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        if self.username:
            return self.username
        return self.first_name
