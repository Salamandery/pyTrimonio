from django.contrib import admin

from pyTrimonio.estoques.models import Estoque

# Register your models here.
class EstoqueAdmin(admin.ModelAdmin):
    list_display = [
        'description', 'created_at', 'updated_at'
    ]
    search_fields = ['description']

admin.site.register(Estoque, EstoqueAdmin)