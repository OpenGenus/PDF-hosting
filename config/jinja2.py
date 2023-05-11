import jinja2
from django.templatetags.static import static
from django.urls import reverse
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_form

from library.forms import BookUploadForm
from library.utils import to_mbs


class Environment:

    def __call__(self, **options):
        env = jinja2.Environment(**options)
        env.globals.update({
            "static": static,
            "url": reverse,
            "crispy": as_crispy_form,
            "book_upload_form": BookUploadForm(),
            "to_mbs": to_mbs,
        })
        return env


environment = Environment()
