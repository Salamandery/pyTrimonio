from django.contrib import admin
from .models import Network

# Register your models here.
class NetworkAdmin(admin.ModelAdmin):
    list_display = [
        'description', 'type',
        'mark', 'sector', 
        'location'
    ]
    search_fields = ['mark', 'sector', 'location', 'type']
    prepopulated_fields = {'description': ('mark','model','type',)}

admin.site.register(Network, NetworkAdmin)