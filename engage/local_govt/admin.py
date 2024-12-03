from django.contrib import admin

from engage.local_govt.models import Localgovt


@admin.register(Localgovt)
class LocalgovtAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'division', 'district', 'upazila', 'union', 'location', 'description']
    search_fields = ['type']
    ordering = ['type']
