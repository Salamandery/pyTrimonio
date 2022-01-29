from django.db import models

class ImpressoraManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(mark__icontains=query) | \
            models.Q(model__icontains=query)
        )