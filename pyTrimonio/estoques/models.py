from django.db import models

from pyTrimonio.estoques.manager import EstoqueManager

# Create your models here.
class Estoque(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    description = models.CharField('Descrição', max_length=200, blank=True, null=True)
    company = models.CharField('Empresa', max_length=100)

    objects = EstoqueManager()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
        ordering = ['company']