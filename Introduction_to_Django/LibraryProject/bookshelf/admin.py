from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Displays columns in the admin list view
    search_fields = ("title", "author")  # Enables searching by title and author
    list_filter = ("publication_year",)  # Adds filtering by publication year

# Alternative way without the decorator:
# admin.site.register(Book, BookAdmin)
