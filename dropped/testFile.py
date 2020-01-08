from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
from sklearn import preprocessing
from textToArr import text_to_arr
from webscrapever2 import get_urls, crawl_hot


training_data = []
words, labels, post_len = text_to_arr('testData.txt')
le = preprocessing.LabelEncoder()
le.fit(words)
# print(words)
transformed_words = le.transform(words).reshape(-1, 1)
# print(transformed_words)

arr_len = len(transformed_words)

for x in range(arr_len):
    training_data.append([transformed_words[x], post_len[x]])


clf = tree.DecisionTreeClassifier()
test = clf.fit(training_data, labels)
#
# words_prob = []
# urls = get_urls('https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/', 1, 2)
# crawl_hot(urls, words_prob, "testing.txt")

words, _, post_len = text_to_arr("testing.txt")
transformed_words = le.transform(words).reshape(-1, 1)
arr_len = len(transformed_words)
test_data = []
for x in range(arr_len):
    test_data.append([transformed_words[x], post_len[x]])

pred_data = clf.predict(test_data)
pred_data = [int(x) for x in pred_data]
count = 0
for item in test_data:
    print('{} - {}'.format(item, pred_data[count]))
    count += 1
