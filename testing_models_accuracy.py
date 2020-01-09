import pandas as pd
import ModelPrediction as m
import ModelPrediction1 as mc
from sklearn import linear_model, naive_bayes, svm
from sklearn import ensemble
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split


train = pd.read_csv("csvData2.csv")

# learning = m.ModelPrediction(train["words"], train["label"], linear_model.LogisticRegression())
# learning.model_testing_tfidf()
# learning.train_model()
#
#
# learning2 = m.ModelPrediction(train["hashtags"], train["label"], linear_model.LogisticRegression())
# learning2.model_testing_tfidf()
# learning2.train_model()
#
#
# words_value = [x[1] for x in learning.predictions_proba]
# words_count = train["words_count"]
# hashtags_value = [x[1] for x in learning2.predictions_proba]
# hashtags_count = train["hashtags_count"]


# linear classifier on Word Level tfidfs
word_level_tfidf_linear = mc.ModelPrediction(train["words"], train["label"],
                                             linear_model.LogisticRegression())
print("\n\nword_level_tfidf_linear")
word_level_tfidf_linear.show_all()

ngram_level_tfidf = mc.ModelPrediction(train["words"], train["label"],
                                       linear_model.LogisticRegression(),
                                       ngrams=(2,3))
print("\nngram_level_tfidf_linear")
ngram_level_tfidf.show_all()

char_level_tfidf = mc.ModelPrediction(train["words"], train["label"],
                                      linear_model.LogisticRegression(),
                                      analyze='char', ngrams=(2,3))
print("\nchar_level_tfidf_linear")
char_level_tfidf.show_all()


# random forest classifier on tfidfs
word_level_tfidf_forest = mc.ModelPrediction(train["words"], train["label"],
                                             ensemble.RandomForestClassifier())
print("\n\nword_level_tfidf_forest")
word_level_tfidf_forest.show_all()

ngram_level_tfidf_forest = mc.ModelPrediction(train["words"], train["label"],
                                              ensemble.RandomForestClassifier(),
                                              ngrams=(2,3))
print("\nngram_level_tfidf_forest")
ngram_level_tfidf_forest.show_all()

char_level_tfidf_forest = mc.ModelPrediction(train["words"], train["label"],
                                             ensemble.RandomForestClassifier(),
                                             analyze='char', ngrams=(2,3))
print("\nchar_level_tfidf_forest")
char_level_tfidf_forest.show_all()


# Naive Bayes classifier on tfidfs
word_level_tfidf_nb = mc.ModelPrediction(train["words"], train["label"],
                                         naive_bayes.MultinomialNB())
print("\n\nword_level_tfidf_nb")
word_level_tfidf_nb.show_all()

ngram_level_tfidf_nb = mc.ModelPrediction(train["words"], train["label"],
                                          naive_bayes.MultinomialNB(),
                                          ngrams=(2,3))
print("\nngram_level_tfidf_nb")
ngram_level_tfidf_nb.show_all()

char_level_tfidf_nb = mc.ModelPrediction(train["words"], train["label"],
                                         naive_bayes.MultinomialNB(),
                                         analyze='char', ngrams=(2,3))
print("\nchar_level_tfidf_nb")
char_level_tfidf_nb.show_all()

# SVM classifier on tfidfs - need to turn off predict_proba in train_model to make it work
# word_level_tfidf_svm = mc.ModelPrediction(train["words"], train["label"],
#                                           svm.SVC())
# print("\n\nword_level_tfidf_svm")
# word_level_tfidf_svm.show_all()
#
# ngram_level_tfidf_svm = mc.ModelPrediction(train["words"], train["label"],
#                                            svm.SVC(),
#                                            ngrams=(2,3))
# print("\nngram_level_tfidf_svm")
# ngram_level_tfidf_svm.show_all()
#
# char_level_tfidf_svm = mc.ModelPrediction(train["words"], train["label"],
#                                           svm.SVC(),
#                                           analyze='char', ngrams=(2,3))
# print("\nchar_level_tfidf_svm")
# char_level_tfidf_svm.show_all()
