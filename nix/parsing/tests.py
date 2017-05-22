from rest_framework.test import APIRequestFactory, APITestCase
from django.core.urlresolvers import reverse
from django.test import TestCase
from parsing.models import Article
from parsing.views import PostList
from parsing.utils import parse
from parsing.tasks import task


class ArticlesTest(APITestCase):
    """
    Testing that:
        - can get all Articles using GET request with no parameters
        - can filter by site URL
    """

    fixtures = ['posts.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PostList.as_view()
        self.created_files = []

    def test_get_posts_all(self):
        """
        Test if we can GET all events (should be 20 from fixtures)
        """
        request = self.factory.get(reverse('posts-list'))
        response = self.view(request)
        self.assertEqual(len(response.data['posts']), 30)

    def test_get_posts_filter_by_site(self):
        """
        Test if we can GET posts filtered by site (2 posts with this site in fixtures)
        """
        request = self.factory.get(reverse('posts-site-list', kwargs={'site': 'theguardian.com'}))
        response = self.view(request, site='theguardian.com')
        self.assertEqual(len(response.data['posts']), 2)


class ParseTest(TestCase):
    def setUp(self):
        parse(3)

    def test_posts_count(self):
        """Parsing creates object for every post"""
        self.assertEqual(len(Article.objects.all()), 90)


class TaskTest(TestCase):
    def setUp(self):
        task(2)

    def test_posts_count(self):
        """Task creates object for every post"""
        self.assertEqual(len(Article.objects.all()), 60)

