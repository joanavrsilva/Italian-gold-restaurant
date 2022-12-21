# Generated by Django 3.2 on 2022-12-21 14:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_remove_booking_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
