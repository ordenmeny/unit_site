from django.db import models
from django.contrib.auth.models import AbstractUser
from pytils.translit import slugify
import os


class CustomUser(AbstractUser):
    social_link = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=512, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='users/')

    def save(self, *args, **kwargs):
        self.username = f'{self.first_name}{self.last_name}{self.pk}'

        if self.image:
            name, extension = os.path.splitext(self.image.name)

            title = slugify(self.first_name + self.last_name + str(self.pk))
            self.image.name = title + extension

        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
