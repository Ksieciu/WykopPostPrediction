from bs4 import BeautifulSoup
from stringFunctions import get_label, get_clear_text
from os import path
import requests
import csv


class Scraper():

    url = "https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/"

    def __init__(self, file_name, page_start=1, page_end=20):
        self.file_name = file_name
        self.page_start = page_start
        self.page_end = page_end


    # https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/
    # getting content from pages
    def start(self):
        for i in range(self.page_start, self.page_end + 1):
            page_url = self.url + str(i)
            print(page_url)
            self.crawl_hot(page_url)


    def crawl_hot(self, url):
        try:
            result = requests.get(url)
        except:
            return 0

        # print(result.status_code)
        content = result.content
        soup = BeautifulSoup(content, 'lxml')
        label = get_label(url)

        # saving data to file using with - we can remove it later, just testing purpose
        # klasa do otwierania i pracowania na otwartym tekście
        self.scrape_page(soup, label)


    def scrape_page(self, soup, label):
        if path.exists(self.file_name):
            exists = True
        else:
            exists = False

        with open(self.file_name, "a+", encoding='utf-8', newline='') as file:
            # looking for div class "wblock lcontrast dC" content - takes post and comments
            writer = csv.writer(file)
            # creating csv columns names
            if exists is False:
                writer.writerow(["post", "words", "words_count", "hashtags",
                                 "hashtags_count", "label"])

            for n in soup.find_all(class_='wblock lcontrast dC'):
                if 'data-type="entry"' not in str(n):
                    continue
                raw_text, words_str, words_len, hashtags_str, hashtags_len = get_clear_text(n)
                # post has unique data-type="entry", so we remove comments by skipping
                # them. Then we save hashtags into arr and erase them and after that we remove
                # all other trash data so we have only raw post content now to work on
                writer.writerow([raw_text, words_str, words_len, hashtags_str, hashtags_len, label])
