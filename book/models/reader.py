from django.db import models


class Reader(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
