from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'
