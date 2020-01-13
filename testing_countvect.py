import CountVectorPrediction as cvp
import PostPrediction as pp
import TreeFinalPrediction as tfp
import pandas as pd
from stringFunctions import df_to_arr
from sklearn import linear_model, naive_bayes

# data that will be predicted
post_input = """Pożyczyłam mojemu bratu pieniądze w kwietniu, bo otwierał swoją restaurację. Powiedział, że odda mi do końca sierpnia, ale było coś też przebąkiwane, że do końca roku, no to myślę sobie spoko. Pytam się go pod koniec sierpnia kiedy mi odda, oburzył się i powiedział, że w grudniu. Pytam się w grudniu kiedy odda, to mi wmawia, że umówił się ze mną na początek roku. Zapytałam się go dzisiaj, a on do mnie z pretensjami i krzykiem. Morał jest kurwa taki, nigdy nie pożyczaj swojej rodzinie pieniędzy, bo jeszcze będą mieli do Ciebie wąty, że chcesz je odzyskać... Jeszcze Mama do mnie z pretensjami, że na co mi są tak potrzebne te pieniądze... ughhhhh!!! #rodzina #zalesie"""

# reading data from file
train = pd.read_csv("csvData4.csv")
# preparing post text for further predictions
post = pp.PostPrediction(post_input)
post_df = post.add_to_df()

# creating class prediction with naive bayes classifier
model = cvp.CountVectorPrediction(train, post_df=post_df, classifier=naive_bayes.MultinomialNB())

# getting predictions_proba on words and adding it to dataframe
model.train_cv_model(tag='words')
model.add_all_predictions_to_df(tag='words')
# probability of words in new post
post_words_prob = model.predict_post(tag='words')
post_df['words_prob'] = post_words_prob

# getting predictions_proba on hashtags and adding it to dataframe
model.train_cv_model(tag='hashtags')
model.add_all_predictions_to_df(tag='hashtags')
# probability of hashtags in new post
post_hashtags_prob = model.predict_post(tag='hashtags')
post_df['hashtags_prob'] = post_hashtags_prob


# getting new df with columns containing predictions_proba on words and hashtags
features_df = model.get_df()

final = tfp.TreeFinalPrediction(features_df)
final.tree_prediction(post_df)
# final.train_test()
final.show_probabilities()
