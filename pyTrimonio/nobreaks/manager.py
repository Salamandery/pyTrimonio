from django.db import models

class NobreakManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(model__icontains=query) | \
            models.Q(mark__icontains=query)
        )