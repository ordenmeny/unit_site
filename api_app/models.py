from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name[:30]
