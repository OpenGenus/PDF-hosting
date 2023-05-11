from rest_framework.generics import ListAPIView

from .models import BookAuthor, BookCategory
from .serializers import BookAuthorSerializer, BookCategorySerializer


class BookAuthorSearchAPIView(ListAPIView):
    serializer_class = BookAuthorSerializer

    def get_queryset(self):
        return BookAuthor.objects.filter(name__icontains=self.request.GET.get("q"))


class BookCategorySearchAPIView(ListAPIView):
    serializer_class = BookCategorySerializer

    def get_queryset(self):
        return BookCategory.objects.filter(name__icontains=self.request.GET.get("q"))
