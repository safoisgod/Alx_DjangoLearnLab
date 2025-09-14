from django.contrib import admin
from .models import Book, Author, Library, UserProfile

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
