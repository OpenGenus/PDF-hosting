from rest_framework import serializers

from .models import BookAuthor, BookCategory


class BookAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookAuthor
        fields = ("id", "name")


class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCategory
        fields = ("id", "name")
