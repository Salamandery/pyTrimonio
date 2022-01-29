from django.db import models

class EmpresaManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(description__icontains=query)
        )