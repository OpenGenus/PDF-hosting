from django import forms

from .models import Book, BookAuthor, BookCategory
from .fields import Select2TaggedMultipleChoiceField


def create_authors(names):
    BookAuthor.objects.bulk_create(list(map(lambda name: BookAuthor(name=name), names)))
    return list(map(lambda author: author.id, BookAuthor.objects.filter(name__in=names)))


def create_categories(names):
    BookCategory.objects.bulk_create(list(map(lambda name: BookCategory(name=name), names)))
    return list(map(lambda category: category.id, BookCategory.objects.filter(name__in=names)))


class BookUploadForm(forms.ModelForm):
    authors = Select2TaggedMultipleChoiceField(BookAuthor, create_authors,
                                               widget=forms.SelectMultiple(attrs={"class": "authors-select"}))
    categories = Select2TaggedMultipleChoiceField(BookCategory, create_categories,
                                                  widget=forms.SelectMultiple(attrs={"class": "categories-select"}))

    class Meta:
        model = Book
        fields = ("title", "authors", "categories", "file")


