# Generated by Django 4.2.17 on 2024-12-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0013_alter_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
