from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

from .validators import PDFRequired, NonMaliciousPDFRequired

User = get_user_model()


def book_file_upload_path(instance, filename):
    return "books/{}/{}".format(slugify(instance.title), filename)


def book_cover_image_upload_path(instance, filename):
    return "books/{}/{}".format(slugify(instance.title), filename)


class BookAuthor(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150, unique=True)
    num_of_pages = models.IntegerField(editable=False)
    file_size = models.FloatField(editable=False)
    cover_image = models.ImageField(upload_to=book_cover_image_upload_path, editable=False)
    file = models.FileField(upload_to=book_file_upload_path, validators=(PDFRequired(), NonMaliciousPDFRequired()))
    categories = models.ManyToManyField("BookCategory", related_name="books")
    authors = models.ManyToManyField("BookAuthor", related_name="books")
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", null=True, editable=False)

    @property
    def download_url(self):
        return self.file.url

    @property
    def cover_image_url(self):
        return self.cover_image.url

    def is_uploader(self, user):
        return self.uploader == user

    def __str__(self):
        return self.title
    


class BookCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Book categories"


class DCMAViolationNotice(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="violation_notice")
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book
