# Generated by Django 4.1.7 on 2023-04-05 16:50

from django.db import migrations, models
import library.models
import library.validators


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcategory',
            options={'verbose_name_plural': 'Book categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='', upload_to=library.models.book_cover_image_upload_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='num_of_pages',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(upload_to=library.models.book_file_upload_path, validators=[library.validators.PDFRequired, library.validators.NonMaliciousPDFRequired]),
        ),
    ]
