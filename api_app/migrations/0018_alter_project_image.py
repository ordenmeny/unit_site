# Generated by Django 4.2.17 on 2024-12-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0017_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='some-path/'),
        ),
    ]
