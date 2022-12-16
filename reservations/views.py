from django.shortcuts import render
from django.views import generic
from .models import Booking

# Generic list view
class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8
