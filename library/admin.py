from django.contrib import admin

from .models import Book, BookCategory, BookAuthor

admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(BookAuthor)

