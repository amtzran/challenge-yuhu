from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "random_slug",
        "title",
        "description",
        "due_date",
        "author",
        "created_at",
    ]
    list_filter = ["due_date", "created_at"]
    search_fields = ["title"]
