from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_date')
    search_fields = ('first_name', 'last_name', 'email', 'category')
    list_filter = ('category', 'created_date', 'first_name', 'last_name')