# Generated by Django 3.2 on 2022-12-21 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='slug',
        ),
    ]
