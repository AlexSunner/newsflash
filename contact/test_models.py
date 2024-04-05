from django.test import TestCase
from .models import Contact, CollaborateRequest

# Define a test case class inheriting from Django's TestCase class
class ContactModelTest(TestCase):
    # Set up test data that will be used in multiple test methods
    @classmethod
    def setUpTestData(cls):
        # Create a Contact object with test data
        Contact.objects.create(title='Test Contact', content='Test Content')

    # Define a test method to check if the title field label is correct
    def test_title_label(self):
        # Retrieve the Contact object created in setUpTestData method
        contact = Contact.objects.get(id=1)
        # Retrieve the verbose name of the 'title' field in the Contact model
        field_label = contact._meta.get_field('title').verbose_name
        # Assert that the field label is equal to 'title'
        self.assertEqual(field_label, 'title')