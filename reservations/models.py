from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Submited"), (1, "Accepted"), (2, "Refused"))

HOUR_OPTION = (
    ("11:00", "11:00"),
    ("11:30", "11:30"),
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("13:00", "13:00"),
    ("13:30", "13:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"),
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    ("21:30", "21:30"),
    ("22:00", "22:00"),
    ("22:30", "22:30"),
    ("23:00", "23:00"),
)

PARTY_OPTION = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10"),
)

class Booking(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="restaurant_booking"
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    party = models.IntegerField(choices=PARTY_OPTION, default=2)
    hour = models.CharField(choices=HOUR_OPTION, default='12:00', max_length=10)
    day = models.DateField()
    special_requirements = models.TextField(max_length=250, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-day']

    def __str__(self):
        return f"{self.day} - {self.hour} - {self.title} - {self.last_name}"

class Note(models.Model):
    employee_name = models.CharField(max_length=25)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE,
                                related_name="notes")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Note {self.body} made by {self.employee_name}"