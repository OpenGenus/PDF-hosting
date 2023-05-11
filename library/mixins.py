from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404

from .models import Book


class BookUploaderRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.get_object().is_uploader(self.request.user)


class BookListTemplateContextMixin(object):
    """ A class that allows other views to use the book_list template without worrying about the context data
    native to the book_list template. The mixin is intended to be used by create views, delete views"""

    @property
    def extra_context(self):
        books = Book.objects.all()
        paginator = Paginator(books, settings.MY_MAX_ITEMS_PER_PAGE)
        page_kwarg = "page"
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == "last":
                page_number = paginator.num_pages
            else:
                page_number = 1
        try:
            page = paginator.page(page_number)
        except InvalidPage as e:
            raise Http404("Invalid page (%(page_number)s): %(message)s"
                          % {"page_number": page_number, "message": str(e)}
                          )
        context = {
            "paginator": paginator,
            "page_obj": page,
            "books": page.object_list,
            "is_paginated": page.has_other_pages()
        }
        return context

