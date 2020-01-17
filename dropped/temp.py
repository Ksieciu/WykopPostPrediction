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
# model.show_all()
