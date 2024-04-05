from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post, Comment

class TestPostViews(TestCase):
    # Set up initial data for testing
    def setUp(self):
        # Create a superuser for testing
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        # Create a post for testing
        self.post = Post.objects.create(
            title="Post title",
            author=self.user,
            slug="post-title",
            excerpt="Post excerpt",
            content="Post content",
            status=1
        )

    def test_render_post_detail_page_with_comment_form(self):
        # Make a GET request to the post detail page
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the post title and content are present in the response content
        self.assertIn(b"Post title", response.content)
        self.assertIn(b"Post content", response.content)
        
        # Check if the comment form instance is present in the context
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_comment_edit_view(self):
        # Simulate user authentication
        self.client.force_login(self.user)
        # Create a comment for the post
        comment = Comment.objects.create(post=self.post, author=self.user, body="Test Comment")
        # Edit the comment
        response = self.client.post(reverse('comment_edit', args=[self.post.slug, comment.id]), {'body': 'Updated Comment'})
        # Check if the comment is updated successfully
        self.assertEqual(response.status_code, 302)  # Redirects to post detail page
        updated_comment = Comment.objects.get(pk=comment.id)
        self.assertEqual(updated_comment.body, 'Updated Comment')

    def test_comment_delete_view(self):
        # Simulate user authentication
        self.client.force_login(self.user)
        # Create a comment for the post
        comment = Comment.objects.create(post=self.post, author=self.user, body="Test Comment")
        # Delete the comment
        response = self.client.post(reverse('comment_delete', args=[self.post.slug, comment.id]))
        # Check if the comment is deleted successfully
        self.assertEqual(response.status_code, 302)  # Redirects to post detail page
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(pk=comment.id)

    def test_post_list_view(self):
        # Create some posts
        Post.objects.create(title="Post 1", author=self.user, slug="post-1", excerpt="Post 1 excerpt", content="Post 1 content", status=1)
        Post.objects.create(title="Post 2", author=self.user, slug="post-2", excerpt="Post 2 excerpt", content="Post 2 content", status=1)
        # Test if PostList view renders correct template and contains posts
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello_news/index.html')
        self.assertIn(b"Post 1", response.content)
        self.assertIn(b"Post 2", response.content)