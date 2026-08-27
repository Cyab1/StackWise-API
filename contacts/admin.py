from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read', 'is_responded')
    list_filter = ('is_read', 'is_responded', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')