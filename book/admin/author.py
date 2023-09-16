from django.contrib import admin
from book.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'birthdate', 'biography']
