from sklearn import metrics
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def train_model(classifier, feature_vector_train, label, feature_vector_valid, valid_y):
    # fit the training dataset on the classifier
    classifier.fit(feature_vector_train, label)
    # predict the labels on validation dataset
    predictions = classifier.predict(feature_vector_valid)
    # print(feature_vector_train[0])
    # print(classifier.predict_proba(feature_vector_valid[0]))
    # print(predictions[0])
    return metrics.accuracy_score(predictions, valid_y)


def model_testing_tfidf(train_x, valid_x):
    train_x, valid_x, train_y, valid_y = train_test_split(train_x, valid_x, random_state=1)
    encoder = preprocessing.LabelEncoder()
    train_y = encoder.fit_transform(train_y)
    valid_y = encoder.fit_transform(valid_y)

    # creating Term Frequency, Inverse Document Frequenct vector
    tfidf_vect = TfidfVectorizer(encoding='utf-8')
    # need to convert data in train["words"] to unicode to avoid ValueError
    words_to_UType = train_x.values.astype('U')
    # putting tfidf data into variables
    x = tfidf_vect.fit(words_to_UType)
    xtrain_tfidf = x.transform(train_x.values.astype('U'))
    xvalid_tfidf = x.transform(valid_x.values.astype('U'))
    return xtrain_tfidf, xvalid_tfidf, train_x, valid_x, train_y, valid_y
