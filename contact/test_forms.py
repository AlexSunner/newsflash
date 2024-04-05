from django.test import TestCase
from .forms import CollaborateForm

class CollaborateFormTest(TestCase):

    def test_collaborate_form_valid(self):
        # Create valid form data
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'This is a test message.',
        }

        # Create form instance with valid data
        form = CollaborateForm(data=form_data)

        # Check if form is valid
        self.assertTrue(form.is_valid())

    def test_collaborate_form_invalid(self):
        # Create invalid form data with no required fields
        form_data = {}

        # Create form instance with invalid data
        form = CollaborateForm(data=form_data)

        # Check if form is invalid
        self.assertFalse(form.is_valid())