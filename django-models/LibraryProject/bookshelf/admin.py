

# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']
    list_filter = ['title']
    search_fields = ['author', 'title',]

admin.site.register(Book, BookAdmin)
