from django.db import models
from .manager import CelularManager

# Create your models here.
class Celular(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    user = models.CharField('Responsável', 
        max_length=50, blank=True, null=True
    )
    mark = models.CharField('Marca', max_length=100)
    model = models.CharField('Modelo', max_length=100, blank=True, null=True)
    serial = models.CharField('Nº Serial', max_length=100, blank=True, null=True)
    identified = models.CharField('Nª Patrimônio', max_length=100, blank=True, null=True)
    description = models.CharField('Descrição', max_length=200, blank=True, null=True)
    number = models.CharField('Linha', max_length=50, blank=True, null=True)
    client = models.CharField('Operadora', max_length=50, blank=True, null=True)
    sector = models.CharField('Setor', max_length=200, blank=True, null=True)
    location = models.CharField('Localidade', max_length=200, blank=True, null=True)

    objects = CelularManager()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Linha / Smartphone'
        verbose_name_plural = 'Linhas / Smartphones'
        ordering = ['mark', 'sector', 'location']