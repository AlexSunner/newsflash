from django.urls import reverse
from django.test import TestCase
from .models import Contact
from .forms import CollaborateForm
from django.contrib.messages import get_messages

class TestContactViews(TestCase):

    def test_successful_collaboration_request_submission(self):
        # Test for a user requesting a collaboration
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('contact'), post_data, follow=True)
        
        # Check if the response redirects to the expected URL
        self.assertRedirects(response, reverse('contact'))

        # Check if success message is displayed in redirected response
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(str(messages[0]), "Collaboration request has been sent successfully!")