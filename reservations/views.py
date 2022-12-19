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
        notes = booking.notes.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking,
                "note": note,
            },
        )
    def booking(self, request, slug, *args, **kwargs):
        queryset = Booking.objects.filter(status=1)
        booking = get_object_or_404(queryset, slug=slug)
        notes = booking.notes.filter(approved=True).order_by("-created_on")
        
        note_form = NoteForm(data=request.POST)
        if note_form.is_valid():
            note_form.instance.email = request.user.email
            note_form.instance.name = request.user.username
            note = note_form.save(commit=False)
            note_form.booking = booking
            booking.save()
        else:
            note_form = NoteForm()

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking,
                "notes": notes,
                "commented": True,
                "note_form": note_form,
            },
        )