from django.contrib import admin

from pyTrimonio.monitores.models import Monitor

# Register your models here.
class MonitorAdmin(admin.ModelAdmin):
    list_display = [
        'serial', 'mark', 
        'sector', 'created_at', 'updated_at'
    ]
    search_fields = ['mark', 'sector']
    prepopulated_fields = {'description': ('mark','model',)}

admin.site.register(Monitor, MonitorAdmin)