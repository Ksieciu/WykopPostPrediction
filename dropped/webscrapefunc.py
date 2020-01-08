from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
from sklearn import preprocessing


post_text = np.array([])
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
def crawl_hot(urls, post_text, post_words_prob):
    for url in urls:
        result = requests.get(url)
        # print(result.status_code)
        content = result.content
        soup = BeautifulSoup(content, 'lxml')



        # saving data to file using with - we can remove it later, just testing purpose
        with open("testData.txt", "a+", encoding='utf-8') as file:
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

                rawText = ''.join([x for x in text if x.isalpha() or x.isspace()])
                words = rawText.lower().split()
                for word in words:
                    if len(word) > 2:
                        post_text = np.append(post_text, words)
                        act_post.append(word)
                        file.write(rawText)

                le = preprocessing.LabelEncoder()
                le.fit(act_post)
                print(act_post)
                print(le.transform(act_post))

                post_len = len(act_post)
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


urls = get_urls('https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/', 1, 1)
crawl_hot(urls, post_text, post_words_prob)

clf = tree.DecisionTreeClassifier()

# clf.fit(post_words_prob, post_words_label)
