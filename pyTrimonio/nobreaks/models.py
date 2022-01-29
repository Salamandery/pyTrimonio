from django.db import models

from pyTrimonio.nobreaks.manager import NobreakManager

# Create your models here.
class Nobreak(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    serial = models.CharField('Serial', max_length=100)
    mark = models.CharField('Marca', max_length=100)
    model = models.CharField('Modelo', max_length=100)
    identified = models.CharField('Nº Patrimônio', max_length=100)
    description = models.CharField('Descrição', max_length=100)
    sector = models.CharField('Setor', max_length=200)
    location = models.CharField('Localidade', max_length=200)

    objects = NobreakManager()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Nobreak'
        verbose_name_plural = 'Nobreaks'
        ordering = ['model', 'sector'] 