from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "date")
    list_display_links = ("name",)
    list_filter = ("name", "email", "date")
    search_fields = ("name", "email")
    readonly_fields = ("name", "email")

