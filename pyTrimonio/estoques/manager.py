from django.db import models

class EstoqueManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(description__icontains=query) | \
            models.Q(company__icontains=query)
        )