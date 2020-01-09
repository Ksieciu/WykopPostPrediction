from ModelPrediction1 import ModelPrediction as mc
from stringFunctions import list_to_string, lemmatize_words
from sklearn import linear_model, naive_bayes, tree
import pandas as pd
import itertools


class PostPrediction():

    def __init__(self, post_input):
        self.post_input = post_input
        self.act_post = []
        self.hashtags = []
        self.words = []
        self.lemmatized = []
        self.hashtags_len = 0
        self.words_len = 0

    def get_data_from_post(self):
        self.raw_text = ''
        self.raw_text = (''.join([x for x in self.post_input if x.isalpha() or x.isspace()])).strip()

        self.words = self.raw_text.lower().split()

        for word in self.words:
            if word[0] == '#':
                self.hashtags.append(word[1:])
            if len(word) > 2:
                self.act_post.append(word)

        self.hashtags_len = len(self.hashtags)
        self.hashtags_str = list_to_string(self.hashtags)

        self.lemmatized = lemmatize_words(self.act_post)
        self.words_len = len(self.act_post)
        self.words_str = list_to_string(self.lemmatized)

    def add_to_df(self):
        self.data = {'raw_text': [self.raw_text],
                     'words': [self.words_str],
                     'words_len': [self.words_len],
                     'hashtags': [self.hashtags_str],
                     'hashtags_len': [self.hashtags_len]}

        self.df = pd.DataFrame(self.data, columns=['raw_text', 'words', 'words_len', 'hashtags', 'hashtags_len'])

    # def predicting(self):
    #     self.word_tfidf_nb = mc.ModelPrediction(self.df["words"], self.df["label"],
    #                                             naive_bayes.MultinomialNB())
    #     self.hashtag_tfidf_nb = mc.ModelPrediction(self.df["hashtags"], self.df["label"],
    #                                                naive_bayes.MultinomialNB())
    #
    #     self.words_value = [x[1] for x in self.word_tfidf_nb.predictions_proba]
    #     self.words_count = self.df["words_count"]
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
