from django.shortcuts import render
from django.views import generic, View
from .models import Booking

# Generic list view
class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class BookingDetail(View):

    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(status=1)
        booking = get_object_or_404(queryset)
        customers = booking.customers.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking,
                "customers": customers,
            },
        )