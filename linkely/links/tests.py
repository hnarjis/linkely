from django.test import TestCase
from .models import Article
from .scraper import guess_title

class ArticleTestCase(TestCase):
    def test_to_string(self):
        article = Article.objects.create(title='example', url='http://www.example.com')
        self.assertEqual(str(article), 'example - http://www.example.com')

class ScraperTestCase(TestCase):
    def test_title_can_be_guessed(self):
        title = guess_title(None, 'http://www.example.com/hello/this_is_an_article-example')
        self.assertEqual(title, 'This is an article example')
