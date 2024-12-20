# Generated by Django 4.2.17 on 2024-12-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0023_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
