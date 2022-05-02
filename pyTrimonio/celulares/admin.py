from django.contrib import admin
from .models import Celular

# Register your models here.
class CelularAdmin(admin.ModelAdmin):
    list_display = [
        'description', 'number',
        'mark', 'sector', 
        'location'
    ]
    search_fields = ['mark', 'sector', 'location', 'user']
    prepopulated_fields = {'description': ('user','model',)}

admin.site.register(Celular, CelularAdmin)