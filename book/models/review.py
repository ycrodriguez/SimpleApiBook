from django.db import models


class Review(models.Model):
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    reader = models.ForeignKey('book.Reader', on_delete=models.CASCADE)
    qualification = models.CharField(max_length=2, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.reader}'
