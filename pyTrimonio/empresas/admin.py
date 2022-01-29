from django.contrib import admin

from pyTrimonio.empresas.models import Empresa

# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display = [
        'description', 'created_at', 'updated_at'
    ]
    search_fields = ['description']

admin.site.register(Empresa, EmpresaAdmin)