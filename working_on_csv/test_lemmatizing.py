from stringFunctions import lemmatize_words
import unittest


class TestLemmatizing(unittest.TestCase):

    def test_lemmatizing(self):
        test_string = "Nikt gdzieś możliwe dba"
        words_list = test_string.split()
        lemmatized = lemmatize_words(words_list)
        self.assertEqual(lemmatized, ['nikt', 'gdzie', 'możliwy', 'dbać'])


if __name__ == '__main__':
    unittest.main()
