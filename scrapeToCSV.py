from bs4 import BeautifulSoup
from stringFunctions import get_urls, lemmatize_words, list_to_string
from os import path
import requests
import csv


# https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/
# getting content from pages
def crawl_hot(urls, file_name):
    for url in urls:
        result = requests.get(url)
        # print(result.status_code)
        content = result.content
        soup = BeautifulSoup(content, 'lxml')
        label = 1
        page = ''
        for x in url[-2:]:
            for y in x:
                if y.isdigit():
                    page = page + y

        if int(page) >= 10:
            label = 0
        else:
            label = 1

        # saving data to file using with - we can remove it later, just testing purpose
        # klasa do otwierania i pracowania na otwartym tekście
        if path.exists("csvData.csv"):
            exists = True
        else:
            exists = False

        with open(file_name, "a+", encoding='utf-8', newline='') as file:
            # looking for div class "wblock lcontrast dC" content - takes post and comments
            writer = csv.writer(file)
            # creating csv columns names
            if exists is False:
                writer.writerow(["post", "words", "words_count", "hashtags",
                                 "hashtags_count", "label"])

            for n in soup.find_all(class_='wblock lcontrast dC'):
                act_post = []
                hashtags = []
                words = []
                hashtags_len = 0
                # post has unique data-type="entry", so we remove comments by skipping
                # them. Then we save hashtags into arr and erase them and after that we remove
                # all other trash data so we have only raw post content now to work on
                if 'data-type="entry"' not in str(n):
                    continue

                # saving hashtags to array and then removing from post data
                for hashTag in n.find_all(class_='showTagSummary'):
                    hashtags.append(hashTag.get_text())  # add tags to arr
                    hashTag.decompose()
                hashtags_len = len(hashtags)
                hashtags_str = list_to_string(hashtags)

                # removing trash data
                for link in (n.find_all('a') or n.find_all(class_='show-more')
                             or n.find_all('span', class_='')
                             or n.find_all(class_='affect')):
                    link.decompose()

                for moreTrash in n.find_all(class_='author ellipsis'):
                    moreTrash.decompose()

                for mediaContent in n.find_all(class_='media-content'):
                    mediaContent.decompose()

                # for span in n.find_all('span', class_=''):
                #     span.decompose()

                text = n.get_text()

                # saving to raw_text prepared taxt with only words and spaces
                raw_text = ''
                raw_text = ''.join([x for x in text if x.isalpha() or x.isspace()])

                # making all letters lowercases and adding them to words list
                words = raw_text.lower().split()
                words_len = 0

                # saving to act_post only words that are at least 3 chars long
                for word in words:
                    if len(word) > 2:
                        act_post.append(word)

                lemmatized = lemmatize_words(act_post)
                words_len = len(act_post)
                words_str = list_to_string(lemmatized)

                # saving to csv text, words and number of words that are at least 3 chars long
                # hashtags and number of hashtags and label(0/1)
                writer.writerow([raw_text, words_str, words_len, hashtags_str, hashtags_len, label])


urls = get_urls('https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/', 1, 20)
crawl_hot(urls, "csvData.csv")
