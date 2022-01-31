from django.contrib import admin
from .models import Impressora

# Register your models here.
class ImpressoraAdmin(admin.ModelAdmin):
    list_display = [
        'hostname', 'ip',
        'mark', 'sector', 
        'created_at', 'updated_at'
    ]
    search_fields = ['mark', 'sector', 'ip', 'hostname']
    prepopulated_fields = {'description': ('hostname','mark',)}

admin.site.register(Impressora, ImpressoraAdmin)