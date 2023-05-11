from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    accepted_terms_of_service = forms.BooleanField(label="Agree to terms of service")

    def clean_accepted_terms_of_service(self, accepted_terms_of_service):
        if not accepted_terms_of_service:
            self.add_error("accepted_terms_of_service", "You must accept the terms of service")
        return accepted_terms_of_service
