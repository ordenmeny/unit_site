# Generated by Django 4.2.17 on 2024-12-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0015_remove_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
