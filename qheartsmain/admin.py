from django.contrib import admin
from .models import RescueReport

@admin.register(RescueReport)
class RescueReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'animal_type', 'behavior', 'created_at')
    list_filter = ('animal_type', 'behavior')
    search_fields = ('name', 'email', 'animal_type')
