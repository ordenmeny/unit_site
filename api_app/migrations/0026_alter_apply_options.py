# Generated by Django 4.2.17 on 2024-12-19 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0025_alter_apply_links_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apply',
            options={'verbose_name': 'Заявки', 'verbose_name_plural': 'Заявки'},
        ),
    ]
