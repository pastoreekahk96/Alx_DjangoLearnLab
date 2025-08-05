from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns in list view
    list_filter = ('publication_year',)  # Filter books by year
    search_fields = ('title', 'author')  # Search by title or author

admin.site.register(Book, BookAdmin)

