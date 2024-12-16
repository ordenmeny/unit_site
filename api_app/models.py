from django.contrib.auth import get_user_model
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name[:30]

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'События'


class News(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now=True, null=True, blank=True)
    # image ...

    def __str__(self):
        return self.title[:30]

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'



class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    link = models.URLField(null=True, blank=True)
    # image ...

    def __str__(self):
        return self.name[:30]

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'


class Apply(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    links_text = models.TextField()
    reason = models.TextField()

    def __str__(self):
        return self.name