from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_date', 'show', 'category')
    list_editable = ('first_name', 'last_name', 'email', 'category', 'show')
    list_filter = ('category', 'created_date', 'first_name', 'last_name')
    list_display_links = None
    search_fields = ('first_name', 'last_name', 'email', 'category')
    list_per_page = 10
    list_max_show_all = 200