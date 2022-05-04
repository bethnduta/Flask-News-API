import unittest
from app.models import Article, Sources

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the articles
    '''
    def setUp(self):
        