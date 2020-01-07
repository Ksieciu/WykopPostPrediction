import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
from sklearn import preprocessing


def text_to_arr(textFile):
    words = []
    labels = []
    post_len = []

    with open(textFile, "r", encoding='utf-8') as file:
        data = file.read()
        data = data.split('\n')
        words = data[::3]
        labels = data[1::3]
        post_len = data[2::3]

        words = words[:-1]

    return words, labels, post_len
    # le = preprocessing.LabelEncoder()
    # # print(words)
    # le.fit(words)
    # print(le.transform(words))
