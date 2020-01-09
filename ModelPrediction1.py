from sklearn import metrics
from sklearn import preprocessing, tree
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import itertools



class ModelPrediction():

    def __init__(self, words, label, classifier, ngrams=(1, 1), analyze='word'):
        self.words = words
        self.label = label
        self.classifier = classifier
        self.ngrams = ngrams
        self.analyze = analyze

    # func for splitting data into training and test sets, and fitting into tfidf method
    def model_testing_tfidf(self):
        # splitting data into training and test sets
        self.train_x, self.valid_x, self.train_label, self.valid_label = train_test_split(self.words, self.label, random_state=1)

        # normalizing labels - not really necessary in our case, but just to be sure
        encoder = preprocessing.LabelEncoder()
        self.train_label = encoder.fit_transform(self.train_label)
        self.valid_label = encoder.fit_transform(self.valid_label)

        # creating Term Frequency, Inverse Document Frequenct vector
        self.tfidf_vect = TfidfVectorizer(encoding='utf-8', analyzer=self.analyze, ngram_range=self.ngrams)
        # need to convert data in train["words"] to unicode to avoid ValueError
        self.words_to_UType = self.train_x.values.astype('U')
        # putting tfidf data into variables
        self.x = self.tfidf_vect.fit(self.words_to_UType)
        self.xtrain_tfidf = self.x.transform(self.train_x.values.astype('U'))
        self.xvalid_tfidf = self.x.transform(self.valid_x.values.astype('U'))
        # return xtrain_tfidf, xvalid_tfidf, train_x, valid_x, train_label, valid_label


    def train_model(self):
        # fit the training dataset on the classifier
        self.classifier.fit(self.xtrain_tfidf, self.train_label)
        # predict the labels on validation dataset(0/1)
        self.predictions = self.classifier.predict(self.xvalid_tfidf)
        # proba gives us an aray of exact probability(0-1) of word
        self.predictions_proba = self.classifier.predict_proba(self.xvalid_tfidf)
        self.accuracy = metrics.accuracy_score(self.predictions, self.valid_label)


    def show_all(self):
        self.model_testing_tfidf()
        self.train_model()
        print("Accuracy:", self.accuracy)
        # print(self.predictions_proba)


    # def post_prediction(self):
    #     self.model_testing_tfidf()
    #     self.train_model()
    #     self.words_value = [x[1] for x in self.word_tfidf_nb.predictions_proba]
    #     self.words_count = self.df["words_count"]
    #
    #     self.model_testing_tfidf()
    #     self.train_model()
    #     self.hashtags_value = [x[1] for x in self.hashtag_tfidf_nb.predictions_proba]
    #     self.hashtags_count = self.df["hashtags_count"]
    #
    #
    # def decision_tree_pred(self, train_df):
    #     self.train_features = [[a,b,c,d] for a,b,c,d in itertools.izip(self.words_value, self.words_count,
    #                                                                    self.hashtags_value, self.hashtags_count)]
    #     self.train_label = train_df['label']
    #     dt_clf = tree.DecisionTreeClassifier()
        #     dt_clf.fit(self.train_features, self.train_label)
