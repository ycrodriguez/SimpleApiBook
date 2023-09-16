from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.ManyToManyField('book.Author')
    gender = models.ForeignKey('book.Gender', on_delete=models.CASCADE)
    year_publication = models.IntegerField()
    editorial = models.ForeignKey('book.Editorial', on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
