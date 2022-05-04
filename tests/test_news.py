import unittest
from app.models import Articles, Sources

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the articles
    '''
    def setUp(self):
        '''
        setUp method to run before the test
        '''
        self.new_article = Articles("abc","Beth","test_title","test_description")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))    
