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

class Booking(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    party = models.ForeignKey('Client', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.DateField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

        def __str__(self):