from django.db import models
from .manager import CrManager
from pyTrimonio.computadores.models import Computador

# Create your models here.
class Cr(Computador):

    objects = CrManager()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Cr'
        verbose_name_plural = 'Cr\'s'
        ordering = ['mark', 'sector']