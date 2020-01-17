from stringFunctions import lemmatize_words, get_clear_text, df_to_arr
from Scraper import Scraper
import unittest
import pandas as pd


class TestingFunctions(unittest.TestCase):

    def test_lemmatizing(self):
        test_string = "Nikt gdzieś możliwe dba"
        words_list = test_string.split()
        lemmatized = lemmatize_words(words_list)
        self.assertEqual(lemmatized, ['nikt', 'gdzie', 'możliwy', 'dbać'])

    def test_url(self):
        test_class = Scraper("csvData3.csv", 1, 2)
        self.assertEqual(test_class.crawl_hot("wololo"), 1)

    # def test_clearing_text(self):
    #     test_string = """<a class="showTagSummary" href="https://www.wykop.pl/tag/polityka">polityka</a>!@#Olaboga!§Üa♂сука блять"""
    #     _, cleared, _, _, _ = get_clear_text(test_string)
    #     print(cleared)
    #     self.assertEqual(cleared, 'olaboga')

    def test_df_to_arr(self):
        d = {'words_prob': [1, 0], 'words_count': [12, 13], 'hashtags_prob': [0.5, 1], 'hashtags_count': [2, 4]}
        df = pd.DataFrame(data=d)
        feat, labels = df_to_arr(df)
        self.assertEqual(feat, [[1, 12, 0.5, 2], [0, 13, 1.0, 4]])





if __name__ == '__main__':
    unittest.main()
