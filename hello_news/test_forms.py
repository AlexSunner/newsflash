from django.test import TestCase
from .forms import CommentForm

class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        # Create a CommentForm instance with some sample data
        comment_form = CommentForm({'body': 'This is a great post'})
        
        # Check if the form is valid
        is_valid = comment_form.is_valid()
        
        # Assert that the form is valid
        self.assertTrue(is_valid, msg="Form is valid")