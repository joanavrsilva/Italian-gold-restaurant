from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking

# Generic list view
class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class BookingDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Booking.objects.filter(status=1)
        booking = get_object_or_404(queryset, slug=slug)
        customers = booking.customers.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking,
                "customer": customer,
            },
        )
    def booking(self, request, slug, *args, **kwargs):

        queryset = Booking.objects.filter(status=1)
        booking = get_object_or_404(queryset, slug=slug)
        customers = booking.customers.filter(approved=True).order_by("-created_on")
        
        customer_form = CustomerForm(data=request.POST)
        if customer_form.is_valid():
            customer_form.instance.email = request.user.email
            customer_form.instance.name = request.user.username
            customer = customer_form.save(commit=False)
            customer_form.booking = booking
            booking.save()
        else:
            customer_form = CustomerForm()

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking,
                "customers": customers,
                "commented": True,
                "customer_form": customer_form,
            },
        )