# Generated by Django 3.2 on 2022-12-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20221218_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_name',
            field=models.CharField(max_length=25),
        ),
    ]