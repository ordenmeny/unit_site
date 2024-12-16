import os

from django.contrib.auth import get_user_model
from django.db import models
from transliterate import translit
from pytils.translit import slugify


class News(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, unique=True)
    text = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='news/')

    def __str__(self):
        return self.title[:30]

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):
        if self.image:
            name, extension = os.path.splitext(self.image.name)

            title = slugify(self.title)
            self.image.name = title + extension

        super(News, self).save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=1000)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='projects/')

    def __str__(self):
        return self.name[:30]

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'

    def save(self, *args, **kwargs):
        if self.image:
            name, extension = os.path.splitext(self.image.name)

            title = slugify(self.name)
            self.image.name = title + extension

        super(Project, self).save(*args, **kwargs)


class Apply(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    links_text = models.TextField()
    reason = models.TextField()

    def __str__(self):
        return self.name


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
