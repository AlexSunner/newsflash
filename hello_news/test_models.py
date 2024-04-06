from django.test import TestCase
from .models import Post, Comment, Category
from django.contrib.auth.models import User


class TestHelloNewsModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        user = User.objects.create_user(username='testuser', password='12345')
        
        # Create a category
        category = Category.objects.create(name='Test Category', slug='test-category')

        # Create a post
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=user,
            content='Test content',
            category=category,
            status=1,
            excerpt='Test excerpt'
        )

        # Create a comment
        comment = Comment.objects.create(
            post=post,
            author=user,
            body='Test comment'
        )

    def test_post_creation(self):
        post = Post.objects.get(slug='test-post')
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.author.username, 'testuser')
        self.assertEqual(post.content, 'Test content')
        self.assertEqual(post.category.name, 'Test Category')
        self.assertEqual(post.status, 1)
        self.assertEqual(post.excerpt, 'Test excerpt')

    def test_comment_creation(self):
        comment = Comment.objects.get(body='Test comment')
        self.assertEqual(comment.post.title, 'Test Post')
        self.assertEqual(comment.author.username, 'testuser')
        self.assertEqual(comment.body, 'Test comment')

    def test_category_creation(self):
        category = Category.objects.get(slug='test-category')
        self.assertEqual(category.name, 'Test Category')
