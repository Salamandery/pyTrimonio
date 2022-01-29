from django.contrib import admin

from .models import Nobreak

# Register your models here.
class NobreakAdmin(admin.ModelAdmin):
    list_display = [
        'mark', 'serial',
        'sector', 'created_at', 'updated_at'
    ]
    search_fields = ['mark', 'sector']

admin.site.register(Nobreak, NobreakAdmin)