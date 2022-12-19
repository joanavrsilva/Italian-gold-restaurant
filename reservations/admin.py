from django.contrib import admin
from .models import Booking, Note
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    summernote_fields = ('special_requirements')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('slug', 'day', 'last_name', 'title', 'created_on')
    list_filter = ('status', 'created_on', 'author', 'day')
    search_field = ['author', 'day', 'party', 'hour']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'booking', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('employee_name', 'booking', 'body')
    actions = ['approve_bookings']

    def approve_notes(self, request, queryset):
        queryset.update(approved=True)