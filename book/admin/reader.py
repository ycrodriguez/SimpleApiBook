from django.contrib import admin
from book.models import Reader


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'email']
