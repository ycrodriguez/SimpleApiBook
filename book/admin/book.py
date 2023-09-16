from django.contrib import admin
from book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'gender', 'year_publication', 'editorial', 'price', 'description']
