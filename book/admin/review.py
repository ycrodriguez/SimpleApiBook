from django.contrib import admin
from book.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'reader', 'qualification', 'comment']
