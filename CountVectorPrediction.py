from sklearn import metrics
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn import linear_model, naive_bayes, svm


class CountVectorPrediction():

    def __init__(self, df, classifier=linear_model.LogisticRegression(), post_df=[], analyze='word'):
        self.classifier = classifier
        self.analyze = analyze
        self.df = df
        self.post_df = post_df


    def fit_cv_data(self, tag='words'):
        # splitting data into training and test sets
        train_x, valid_x, train_y, valid_y = train_test_split(self.df[tag], self.df['label'])
        # normalizing labels - not really necessary in our case, but just to be sure
        encoder = preprocessing.LabelEncoder()
        self.train_label = encoder.fit_transform(train_y)
        self.valid_label = encoder.fit_transform(valid_y)
        # creating CountVectorizer, fitting(teaching) and transforming data
        self.count_vect = CountVectorizer(analyzer='word')
        self.xtrain_count = self.count_vect.fit_transform(train_x.astype('U'))
        self.xvalid_count = self.count_vect.transform(valid_x.astype('U'))


    def train_cv_model(self, tag='words'):
        self.fit_cv_data(tag)
        # fit the training dataset on the classifier
        self.classifier.fit(self.xtrain_count, self.train_label)
        # predict the labels on validation dataset(0/1)
        self.predictions = self.classifier.predict(self.xvalid_count)
        # proba gives us an aray of exact probability(0-1) of word

        self.accuracy = metrics.accuracy_score(self.predictions, self.valid_label)
        print("{}: {}".format(self.classifier, self.accuracy))

    def predict_post(self, tag='words'):
        self.post_count = self.count_vect.transform(self.post_df[tag].astype('U'))
        self.predictions = self.classifier.predict(self.post_count)
        self.predictions_proba = self.classifier.predict_proba(self.post_count)
        return self.predictions_proba[0][1]

    # adding results of predictions_proba to dataframe
    def add_all_predictions_to_df(self, tag='words'):
        self.words_prob = []
        self.text = self.count_vect.transform(self.df[tag].astype('U'))
        for i in range(len(self.df)):
            self.text_pred_proba = self.classifier.predict_proba(self.text[i])
            self.words_prob.append(self.text_pred_proba[0][1])
        self.df[tag+'_prob'] = self.words_prob

    # returning dataframe - made for returning dataframe with added predictions_proba
    def get_df(self):
        return self.df

    # show accuracy of model
    def show_all(self):
        print("Accuracy:", self.accuracy)
