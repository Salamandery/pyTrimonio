from django.contrib import admin
from .models import Computador

# Register your models here.
class ComputadorAdmin(admin.ModelAdmin):
    list_display = [
        'hostname', 'ip',
        'mark', 'sector', 
        'location', 'updated_at'
    ]
    search_fields = ['mark', 'sector', 'ip', 'hostname']
    prepopulated_fields = {'description': ('hostname','mark',)}

admin.site.register(Computador, ComputadorAdmin)