from django.db import models


class Editorial(models.Model):
    name = models.CharField(max_length=32)
    country = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'
