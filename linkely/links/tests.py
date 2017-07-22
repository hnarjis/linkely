from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article
from .scraper import guess_title

class ArticleTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test', 'test@test.com', 'secret')
        Article.objects.create(id='1', title='example', url='http://www.example.com', user=user)

    def test_to_string(self):
        article = Article.objects.get(title='example')
        self.assertEqual(str(article), 'example - http://www.example.com')

    def test_as_dict(self):
        article = Article.objects.get(title='example')
        self.assertEqual(Article.as_dict(article), {
            "id": 1,
            "title": 'example',
            "url": 'http://www.example.com',
            "user": 'test'
        })


class ScraperTestCase(TestCase):
    def test_guess_title(self):
        title = guess_title(None, 'http://www.example.com/hello/this_is_an_article-example')
        self.assertEqual(title, 'This is an article example')


class RedirectionTestCase(TestCase):
    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_index_redirection(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/login?next=/')

    def test_user_redirection(self):
        response = self.client.get('/links/user/test')
        self.assertRedirects(response, '/login?next=/links/user/test')

    def test_add_redirection(self):
        response = self.client.post('/links/add')
        self.assertRedirects(response, '/login?next=/links/add')

    def test_search_redirection(self):
        response = self.client.post('/links/search')
        self.assertRedirects(response, '/login?next=/links/search')


class LoginTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test', 'test@test.com', 'secret')
        self.client.login(username='test', password='secret')

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_redirection(self):
        response = self.client.get('/login')
        self.assertRedirects(response, '/')

    def test_existing_user(self):
        response = self.client.get('/links/user/test')
        self.assertEqual(response.status_code, 200)

    def test_non_existing_user(self):
        response = self.client.get('/links/user/nouser')
        self.assertEqual(response.status_code, 404)

    def test_logout(self):
        response = self.client.get('/logout')
        self.assertRedirects(response, '/login')
