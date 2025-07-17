from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience', 'email', 'is_approved')
    list_filter = ('is_approved', 'specialization')
    search_fields = ('name', 'email')
    list_editable = ('is_approved',)
