from django.urls import path

import library.views as library_views
import library.api_views as library_api_views


api_urlpatterns = [
    path("authors/search", library_api_views.BookAuthorSearchAPIView.as_view(), name="author-search"),
    path("book-categories/search", library_api_views.BookCategorySearchAPIView.as_view(),
         name="book-category-search")
]

urlpatterns = [
    path("books", library_views.BookListView.as_view(), name="book-list"),
    path("books/upload", library_views.BookUploadView.as_view(), name="book-upload"),
    path("books/<int:book_id>/update", library_views.BookUpdateView.as_view(), name="book-update"),
    path("books/<int:book_id>/delete", library_views.BookDeleteView.as_view(), name="book-delete"),
    path("books/<int:book_id>/dcma/report", library_views.DMCAViolationReportView.as_view(), name="dmca-report"),
    path("book-categories", library_views.BookCategoryListView.as_view(), name="book-category-list")
] + api_urlpatterns
