import io
import fitz
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify

from .models import Book


@receiver(pre_save, sender=Book)
def attach_book_meta_data(sender, instance, *args, **kwargs):
    with fitz.Document(stream=io.BytesIO(instance.file.read())) as pdf:
        instance.file.seek(0)
        instance.file_size = instance.file.size
        instance.num_of_pages = pdf.page_count
        cover_image_file = ContentFile(pdf.load_page(0).get_pixmap().tobytes(),
                                       name="{}_cover.png".format(slugify(instance.title)))
        instance.cover_image = cover_image_file
        instance.file.seek(0)  # restore file cursor
