from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    summernote_fields = ('special_requirements')
    list_display = ('first_name', 'last_name', 'day', 'hour', 'created_on')
    list_filter = ('status', 'created_on', 'author', 'day')
    search_field = ['author', 'day', 'party', 'hour']
    