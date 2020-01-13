from sklearn import metrics
from sklearn import model_selection, preprocessing, tree
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import itertools
import pandas as pd
from sklearn import linear_model, naive_bayes, svm
from sklearn import ensemble


class ModelPrediction():

    def __init__(self, df, classifier=linear_model.LogisticRegression(), post_df=[], ngrams=(1, 1), analyze='word'):
        self.words = df['words']
        self.label = df['label']
        self.classifier = classifier
        self.ngrams = ngrams
        self.analyze = analyze
        self.df = df
        self.post_df = post_df

    # func for splitting data into training and test sets, and fitting into tfidf method
    def fit_to_CountVectorizer(self):
        # making copy of df and working on copy
        self.for_fit_df = self.df.copy()
        self.for_fit_df = self.for_fit_df.drop('label', axis=1)
        # if post_data passed to class, then add it to df copy
        if self.post_df.empty is False:
            self.for_fit_df = self.for_fit_df.append(self.post_df, ignore_index=True)
        # make CountVectorizer, fit and transform data
        self.count_vect = CountVectorizer(analyzer='word')
        self.words_to_UType = self.for_fit_df['words'].values.astype('U')
        # print(self.post_df)
        self.count_vect.fit(self.words_to_UType)
        self.data_transformed = self.count_vect.transform(self.words_to_UType)
        # split transformed data into post data and train data(data_transformed will be traning set)
        self.post_transformed = self.data_transformed[-1]
        self.data_transformed = self.data_transformed[:-1]
        print(self.post_transformed)
        print(self.data_transformed)

    def fit_cv_data(self):
        self.fit_to_CountVectorizer()
        # splitting data into training and test sets
        self.train_x, self.valid_x, self.train_y, self.valid_y = model_selection.train_test_split(self.data_transformed, self.df['label'])
        # normalizing labels - not really necessary in our case, but just to be sure
        self.encoder = preprocessing.LabelEncoder()
        self.train_label = self.encoder.fit_transform(self.train_y)
        self.valid_label = self.encoder.fit_transform(self.valid_y)
        # creating CountVectorizer, fitting and transforming data
        self.count_vect = CountVectorizer(analyzer='word')
        self.xtrain_count = self.count_vect.fit_transform(self.train_x.astype('U'))
        self.xvalid_count = self.count_vect.fit_transform(self.valid_x.astype('U'))
        # print(self.xtrain_count)


    def train_cv_model(self):
        self.fit_cv_data()
        # fit the training dataset on the classifier
        self.classifier.fit(self.xtrain_count, self.train_label)
        # predict the labels on validation dataset(0/1)
        self.predictions = self.classifier.predict(self.xvalid_count)
        # proba gives us an aray of exact probability(0-1) of word

        self.accuracy = metrics.accuracy_score(self.predictions, self.valid_label)
        # print("{}: {}".format(self.classifier, self.accuracy))

    def predict_post(self):
        self.post_count = self.count_vect.fit_transform(self.post_df['words'].astype('U'))
        print(self.post_count)
        # self.predictions_proba = self.classifier.predict_proba(self.post_count)
        # print(self.predictions_proba)

    # def model_testing_tfidf(self):
    #     # splitting data into training and test sets
    #     self.train_x, self.valid_x, self.train_label, self.valid_label = train_test_split(self.words, self.label, random_state=1)
    #
    #     # normalizing labels - not really necessary in our case, but just to be sure
    #     encoder = preprocessing.LabelEncoder()
    #     self.train_label = encoder.fit_transform(self.train_label)
    #     self.valid_label = encoder.fit_transform(self.valid_label)
    #
    #     # creating Term Frequency, Inverse Document Frequenct vector
    #     self.tfidf_vect = TfidfVectorizer(encoding='utf-8', analyzer=self.analyze, ngram_range=self.ngrams)
    #     # need to convert data in train["words"] to unicode to avoid ValueError
    #     self.words_to_UType = self.train_x.values.astype('U')
    #     # putting tfidf data into variables
    #     self.x = self.tfidf_vect.fit(self.words_to_UType)
    #
    #     self.xtrain_tfidf = self.x.transform(self.train_x.values.astype('U'))
    #     # self.post_tfidf = self.x.transform(self.post_text)
    #     self.xvalid_tfidf = self.x.transform(self.valid_x.values.astype('U'))
    #     # return xtrain_tfidf, xvalid_tfidf, train_x, valid_x, train_label, valid_label
    #
    #
    # def train_test_model(self):
    #     # fit the training dataset on the classifier
    #     self.classifier.fit(self.xtrain_tfidf, self.train_label)
    #     # predict the labels on validation dataset(0/1)
    #     self.predictions = self.classifier.predict(self.xvalid_tfidf)
    #     # proba gives us an aray of exact probability(0-1) of word
    #     self.predictions_proba = self.classifier.predict_proba(self.xvalid_tfidf)
    #     self.accuracy = metrics.accuracy_score(self.predictions, self.valid_label)


    # def show_all(self):
    #     # self.model_testing_tfidf()
    #     # self.train_model()
    #     print("Accuracy:", self.accuracy)
    #     # print(self.predictions_proba)

    # def post_pred(self):
