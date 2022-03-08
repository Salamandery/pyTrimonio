from django.contrib import admin
from .models import Rep

# Register your models here.
class RepAdmin(admin.ModelAdmin):
    list_display = [
        'hostname', 'ip',
        'mark', 'sector', 
        'created_at', 'updated_at'
    ]
    search_fields = ['mark', 'sector', 'ip', 'hostname']
    prepopulated_fields = {'description': ('hostname','mark',)}

admin.site.register(Rep, RepAdmin)