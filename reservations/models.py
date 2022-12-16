from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    featured_image = CloudinaryField('image', default='placeholder')

class Table(models.Model):
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()