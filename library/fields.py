from django import forms


class Select2TaggedMultipleChoiceField(forms.MultipleChoiceField):
    """
    The essence of using a select2 select control is to defer the loading of the choices and provide them as the user
    types in the control, Thus this field shouldn't raise errors for non-existent choices but creates them
    """

    def __init__(self, model, auto_choices_create_fn, *args, **kwargs):
        self.model = model  # Used to find choices that don't exist yet in the database
        self.auto_choices_create_fn = auto_choices_create_fn  # Used to create non-existent choices
        kwargs["choices"] = ()  # Turn off choices
        super().__init__(*args, **kwargs)

    def validate(self, value):
        if self.required and not value:
            raise forms.ValidationError(self.error_messages["required"], code="required")

    def clean(self, value):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)

        non_available_choices = list(filter(lambda v, s=self: s.castable_to_int(v) is False, value))
        possible_available_choices = list(filter(lambda v, s=self: s.castable_to_int(v), value))
        # Filter out any user choices that are not in the database but appear in possible choices(bad input from user)
        available_choices = list(
            map(lambda v: v[0], self.model.objects.filter(pk__in=possible_available_choices).values_list("id")))
        available_choices.extend(self.auto_choices_create_fn(non_available_choices))
        return available_choices

    @staticmethod
    def castable_to_int(value):
        try:
            int(value)
        except ValueError:
            return False
        return True
