import CountVectorPrediction as cvp
import TreeFinalPrediction as tfp


def cv_prediction(_train, _post_df, _classifier):
    # creating class prediction with naive bayes classifier
    model = cvp.CountVectorPrediction(_train, post_df=_post_df, classifier=_classifier)

    # getting predictions_proba on words and adding it to dataframe
    model.train_cv_model(tag='words')
    model.add_all_predictions_to_df(tag='words')
    # probability of words in new post
    post_words_prob = model.predict_post(tag='words')
    _post_df['words_prob'] = post_words_prob

    # getting predictions_proba on hashtags and adding it to dataframe
    model.train_cv_model(tag='hashtags')
    model.add_all_predictions_to_df(tag='hashtags')
    # probability of hashtags in new post
    post_hashtags_prob = model.predict_post(tag='hashtags')
    _post_df['hashtags_prob'] = post_hashtags_prob
    # model.show_all()

    final = tfp.TreeFinalPrediction(model.get_df())
    final.tree_prediction(_post_df)
    final.train_test()
    final.show_probabilities()
