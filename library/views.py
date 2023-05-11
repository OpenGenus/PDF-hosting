from functools import cached_property

from django.urls import reverse_lazy
from django.conf import settings
from django.db import transaction
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Book
from .mixins import BookUploaderRequiredMixin, BookListTemplateContextMixin
from .forms import BookUploadForm


class BookListView(ListView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"
    paginate_by = settings.MY_MAX_ITEMS_PER_PAGE


class BookUpdateView(LoginRequiredMixin, BookUploaderRequiredMixin, UpdateView):
    model = Book
    pk_url_kwarg = "book_id"

    @cached_property
    def get_object(self, queryset=None):
        return super().get_object(queryset)


class BookDeleteView(LoginRequiredMixin, BookUploaderRequiredMixin, DeleteView):
    model = Book

    @cached_property
    def get_object(self, queryset=None):
        return super().get_object(queryset)


class DMCAViolationReportView(SingleObjectMixin, View):
    pk_url_kwarg = "book_id"
    model = Book

    def get(self, request, *args, **kwargs):
        """TODO: Log DCMA violation notice in database and notify the user(if any) that uploaded the book"""
        pass


class BookCategoryListView(ListView):
    model = Book
    template_name = "library/book_category_list.html"
    context_object_name = "book_categories"
    paginate_by = settings.MY_MAX_ITEMS_PER_PAGE


class BookUploadView(SuccessMessageMixin, BookListTemplateContextMixin, CreateView):
    template_name = "library/book_list.html"  # Used incase the form is invalid
    http_method_names = ["post"]
    form_class = BookUploadForm
    success_url = reverse_lazy("home")
    success_message = "Book uploaded successfully"

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        # Overwrite the global variable 'book_upload_form' so that template receives the form with the right state
        # (erroneous form) and not the unbound global form (book_upload_form)
        return self.render_to_response(self.get_context_data(book_upload_form=form))

