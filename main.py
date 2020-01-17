import PostNormalizing as pp
import pandas as pd
from sklearn import linear_model, naive_bayes, ensemble
from testing_countvect import cv_prediction

# data that will be predicted
post_input = """Zastanawiasz sie dlaczego jeszcze nie przyszło Ci stypendium? Ministerstwo nie ma środków do wypłacenia na stypendia rekotorskie oraz socjalne dla studenciaków. Jak tam ten budżet bez deficytu!? XD

Bynajmniej na bombelki dały xDDDD

#studbaza #pis #bekazpisu"""

# reading data from file
train = pd.read_csv("csvData4.csv")
# preparing post text for further predictions
post = pp.PostNormalizing(post_input)
post_df = post.add_to_df()

# getting new df with columns containing predictions_proba on words and hashtags
cv_prediction(train, post_df, naive_bayes.MultinomialNB())
# cv_prediction(train, post_df, linear_model.LogisticRegression())
# cv_prediction(train, post_df, ensemble.RandomForestClassifier())
