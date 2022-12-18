from django.contrib import admin
from .models import Booking, Customer
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    summernote_fields = ('special_requirements')
    list_display = ('first_name', 'last_name', 'day', 'hour', 'created_on')
    list_filter = ('status', 'created_on', 'author', 'day')
    search_field = ['author', 'day', 'party', 'hour']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'booking', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('first_name', 'last_name', 'email', 'body')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)