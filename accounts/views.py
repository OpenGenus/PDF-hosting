from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from library.models import Book

from .forms import RegisterForm


class MyUploadsListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "accounts/my_uploads.html"

    def get_queryset(self):
        return super().get_queryset().filter(uploader=self.request.user)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
