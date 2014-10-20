
from django.core.exceptions import ValidationError
from django.test import TestCase
from date_app.forms import DaterCreationForm
from date_app.models import Dater


class FormTestCase(TestCase):
    def test_clean_username_exception(self):
        # Create a player so that this username we're testing is already taken
        Dater.objects.create_user(username='test-user')

        # set up the form for testing
        form = DaterCreationForm()
        form.cleaned_data = {'username': 'test-user'}

        # use a context manager to watch for the validation error being raised
        with self.assertRaises(ValidationError):
            form.clean_username()