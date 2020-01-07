from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
from sklearn import preprocessing
from textToArr import text_to_arr
from sklearn.model_selection import train_test_split



train = pd.read_csv("csvData.csv")
print(train["hashtags"].head())
# X_train, X_test, y_train, y_test = train_test_split(words, labels, random_state=1)
