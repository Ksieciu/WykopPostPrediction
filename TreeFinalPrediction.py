from sklearn import tree
from stringFunctions import df_to_arr
from sklearn import metrics
from sklearn.model_selection import train_test_split


class TreeFinalPrediction():

    def __init__(self, df):
        self.df = df

    def tree_prediction(self, pred_data):
        self.data = pred_data
        self.features, self.labels = df_to_arr(self.df)
        clf = tree.DecisionTreeClassifier(criterion="gini")
        clf.fit(self.features, self.labels)
        self.pred_post, _ = df_to_arr(self.data)
        self.pred = clf.predict(self.pred_post)
        self.pred_proba = clf.predict_proba(self.pred_post)

    # evaluating model
    def train_test(self):
        X_train, X_test, y_train, y_test = train_test_split(self.features, self.labels, test_size=0.3, random_state=1)
        clf = tree.DecisionTreeClassifier(criterion="gini")
        clf = clf.fit(X_train,y_train)
        y_pred = clf.predict(X_test)
        print("\nAccuracy:", metrics.accuracy_score(y_test, y_pred))

    # show final results of prediction
    def show_probabilities(self):
        print("Wartość użytych słów została oszacowana na:", self.pred_post[0][0])
        print("Wartość użytych hashtagów została oszacowana na:", self.pred_post[0][2])
        print("Ilość użytych słów wyniosła:", self.pred_post[0][1])
        print("Ilość użytych hashtagów wyniosła:", self.pred_post[0][3])
        if self.pred == 1:
            print("Na podstawie tych danych przewiduję, że post dostanie się w gorące.")
        else:
            print("Na podstawie tych danych przewiduję, że post nie dostanie się w gorące.")
