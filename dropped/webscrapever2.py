from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
from sklearn import preprocessing
from textToArr import text_to_arr


num_of_words = []
hashtags = np.array([])
num_of_hashtags = []
images = np.array([[]])

words = []
words_state = []
post_words_prob = []
post_words_label = []



# https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/
# getting content from pages
def crawl_hot(urls, post_words_prob, file_name):
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
        with open(file_name, "a+", encoding='utf-8') as file:
            # looking for div class "wblock lcontrast dC" content - takes post and comments
            for n in soup.find_all(class_='wblock lcontrast dC'):
                act_post = []
                # post has unique data-type="entry", so we remove comments by skipping
                # them. Then we save hashtags into arr and erase them and after that we remove
                # all other trash data so we have only raw post content now to work on
                if 'data-type="entry"' not in str(n):
                    continue

                # saving hashtags to array and then removing from post data
                for hashTag in n.find_all(class_='showTagSummary'):
                    # print(hashTag.text)  # add tags to arr
                    hashTag.decompose()

                # removing trash data
                for link in (n.find_all('a') or n.find_all(class_='show-more')
                             or n.find_all('span', class_='')
                             or n.find_all(class_='affect')):
                    link.decompose()

                for moreTrash in n.find_all(class_='author ellipsis'):
                    moreTrash.decompose()

                for mediaContent in n.find_all(class_='media-content'):
                    mediaContent.decompose()
                    # ADD 1 or 0 to arr 'if had picture'
                # for span in n.find_all('span', class_=''):
                #     span.decompose()

                text = n.get_text()
                # text = str(n)
                rawText = ''
                rawText = ''.join([x for x in text if x.isalpha() or x.isspace()])

                words = rawText.lower().split()
                post_len = 0
                for word in words:
                    if len(word) > 2:
                        act_post.append(word)

                post_len = len(act_post)

                for word in act_post:
                    file.write(word + '\n')
                    file.write(str(label) + '\n')
                    file.write(str(post_len) + '\n')


                # le = preprocessing.LabelEncoder()
                # le.fit(act_post)
                # print(act_post)
                # print(le.transform(act_post))


                for elem in act_post:
                    post_words_prob.append([elem, post_len])
                    post_words_label.append(1)
    # print(post_words_prob)


# func for getting pages urls(ex. urls from pages 1-7) and returning list of urls
def get_urls(page_url, starting_page, ending_page):
    urls = []
    for i in range(starting_page, ending_page+1):
        url = page_url + str(i)
        urls.append(url)
    return urls


urls = get_urls('https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/', 1, 20)
crawl_hot(urls, post_words_prob, "testData.txt")
