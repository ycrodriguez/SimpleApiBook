from django.contrib import admin
from book.models import Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['name']
