import pandas as pd
from sklearn import preprocessing, linear_model
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from models_functions import train_model, model_testing_tfidf


train = pd.read_csv("csvData.csv")
# fitting data into tfidf model
xtrain_tfidf, xvalid_tfidf, train_x, valid_x, train_y, valid_y = model_testing_tfidf(train["words"][1:], train["label"][1:])

# checking model accuracy
accuracy = train_model(linear_model.LogisticRegression(), xtrain_tfidf, train_y, xvalid_tfidf, valid_y)
print("Words Accuracy:", accuracy)

# # same as before but for hashtags
xtrain_tfidf, xvalid_tfidf, train_x, valid_x, train_y, valid_y = model_testing_tfidf(train["hashtags"], train["label"])
accuracy = train_model(linear_model.LogisticRegression(), xtrain_tfidf, train_y, xvalid_tfidf, valid_y)
print("Hashtags Accuracy:", accuracy)
