from django.contrib.auth import get_user_model
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    # is_private = models.BooleanField(default=True)  # Вход свободный или нет?

    def __str__(self):
        return self.name[:30]

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'События'


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_created = models.DateField(auto_now=True)
    # author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    # image ...

    def __str__(self):
        return self.title[:30]

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
