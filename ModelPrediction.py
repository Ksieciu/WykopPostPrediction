from sklearn import metrics
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


class ModelPrediction():

    def __init__(self, data, label, classifier):
        self.data = data
        self.label = label
        self.classifier = classifier

    def model_testing_tfidf(self):
        # splitting data into training and test sets
        self.train_x, self.valid_x, self.train_label, self.valid_label = train_test_split(self.data, self.label, random_state=1)

        # normalizing labels - not really necessary in our case, but just to be sure
        encoder = preprocessing.LabelEncoder()
        self.train_label = encoder.fit_transform(self.train_label)
        self.valid_label = encoder.fit_transform(self.valid_label)

        # creating Term Frequency, Inverse Document Frequenct vector
        tfidf_vect = TfidfVectorizer(encoding='utf-8')
        # need to convert data in train["words"] to unicode to avoid ValueError
        words_to_UType = self.train_x.values.astype('U')
        # putting tfidf data into variables
        x = tfidf_vect.fit(words_to_UType)
        self.xtrain_tfidf = x.transform(self.train_x.values.astype('U'))
        self.xvalid_tfidf = x.transform(self.valid_x.values.astype('U'))
        # return xtrain_tfidf, xvalid_tfidf, train_x, valid_x, train_label, valid_label


    def train_model(self):
        # fit the training dataset on the classifier
        self.classifier.fit(self.xtrain_tfidf, self.train_label)
        # predict the labels on validation dataset
        self.predictions = self.classifier.predict(self.xvalid_tfidf)
        # print(feature_vector_train[0])
        self.predictions_proba = self.classifier.predict_proba(self.xvalid_tfidf)
        # print(predictions[0])
        self.accuracy = metrics.accuracy_score(self.predictions, self.valid_label)


    def show_all(self):
        print("Accuracy:", self.accuracy)
        print(self.predictions_proba)
