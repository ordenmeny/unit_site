# Generated by Django 4.2.17 on 2024-12-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0022_news_image_telegram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='news/'),
        ),
    ]