from django.contrib import admin
from book.models import Editorial


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
