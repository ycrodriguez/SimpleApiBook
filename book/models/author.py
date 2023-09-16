from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    birthdate = models.DateField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
