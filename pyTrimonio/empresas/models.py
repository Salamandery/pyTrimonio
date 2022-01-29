from django.db import models

from pyTrimonio.empresas.manager import EmpresaManager

# Create your models here.
class Empresa(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    description = models.CharField('Descrição', max_length=200, blank=True, null=True)

    objects = EmpresaManager()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['description']