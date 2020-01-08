import pandas as pd
import models_functions as m
from sklearn import linear_model
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split


train = pd.read_csv("csvData2.csv")

learning = m.ModelPrediction(train["words"], train["label"], linear_model.LogisticRegression())
learning.model_testing_tfidf()
learning.train_model()


learning2 = m.ModelPrediction(train["hashtags"], train["label"], linear_model.LogisticRegression())
learning2.model_testing_tfidf()
learning2.train_model()


words_value = [x[1] for x in learning.predictions_proba]
words_count = train["words_count"]
hashtags_value = learning2.predictions_proba
hashtags_count = train["hashtags_count"]

print(type(hashtags_value))



# fitting data into tfidf model
# xtrain_tfidf, xvalid_tfidf, train_x, valid_x, train_label, valid_label = model_testing_tfidf(train["words"], train["label"])
# # checking model accuracy
# accuracy, predictions_proba = train_model(linear_model.LogisticRegression(), xtrain_tfidf, train_label, xvalid_tfidf, valid_label)
# print("Words Accuracy:", accuracy)
# print(predictions_proba)
# # print(len(train_y))
# # print(len(valid_y))
# # # same as before but for hashtags
# xtrain_tfidf, xvalid_tfidf, train_x, valid_x, train_label, valid_label = model_testing_tfidf(train["hashtags"], train["label"])
# accuracy, predictions_proba = train_model(linear_model.LogisticRegression(), xtrain_tfidf, train_label, xvalid_tfidf, valid_label)
# print("Hashtags Accuracy:", accuracy)
# print(predictions_proba)
