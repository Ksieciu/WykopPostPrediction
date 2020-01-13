from stringFunctions import list_to_string, lemmatize_words
from sklearn import linear_model, naive_bayes, tree
import pandas as pd


class PostPrediction():

    def __init__(self, post_input):
        self.post_input = post_input
        self.act_post = []
        self.hashtags = []
        self.words = []
        self.lemmatized = []
        self.words_str = ''
        self.hashtags_len = 0
        self.words_len = 0
        self.get_data_from_post()
        # self.add_to_df()

    def get_data_from_post(self):
        self.raw_text = ''
        self.raw_text = (''.join([x for x in self.post_input if x.isalpha() or x.isspace() or x == '#'])).strip()

        self.words = self.raw_text.lower().split()

        for word in self.words:
            if word[0] == '#':
                self.hashtags.append(word[1:])
            elif len(word) > 2:
                self.act_post.append(word)

        self.hashtags_len = len(self.hashtags)
        self.hashtags_str = list_to_string(self.hashtags)

        self.lemmatized = lemmatize_words(self.act_post)
        self.words_len = len(self.act_post)
        self.words_str = list_to_string(self.lemmatized)

    def add_to_df(self):
        self.data = {'raw_text': [self.raw_text],
                     'words': [self.words_str],
                     'words_count': [self.words_len],
                     'hashtags': [self.hashtags_str],
                     'hashtags_count': [self.hashtags_len]}

        self.df = pd.DataFrame(self.data, columns=['raw_text', 'words', 'words_count', 'hashtags', 'hashtags_count'])
        return self.df
    # poniżej źle, bo nie transformuje tych samych danych
    # def predict_post(self):
    #     self.words_to_UType = self.df['words'].values.astype('U')
    #     self.x = self.obj_words.tfidf_vect.fit(self.words_to_UType)
    #     self.post_tfidf = self.x.transform(self.df['words'].values.astype('U'))
    #     self.post_predictions = self.obj_words.classifier.predict(self.post_tfidf)
    #     print(self.post_predictions)


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
