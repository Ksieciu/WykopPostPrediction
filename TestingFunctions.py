from stringFunctions import lemmatize_words
from Scraper import Scraper
import unittest


class TestingFunctions(unittest.TestCase):

    def test_lemmatizing(self):
        test_string = "Nikt gdzieś możliwe dba"
        words_list = test_string.split()
        lemmatized = lemmatize_words(words_list)
        self.assertEqual(lemmatized, ['nikt', 'gdzie', 'możliwy', 'dbać'])

    def test_url(self):
        test_class = Scraper("csvData3.csv")
        self.assertEqual(test_class.crawl_hot("wololo"), 1)


if __name__ == '__main__':
    unittest.main()
