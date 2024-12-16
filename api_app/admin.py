from django.contrib import admin
from .models import *

admin.site.register(Event)
# admin.site.register(News)
admin.site.register(Project)


class CustomNewsAdmin(admin.ModelAdmin):
    exclude = ['image_telegram']


admin.site.register(News, CustomNewsAdmin)
