-----------------------------------
Before using you need to install:
http://download.sgjp.pl/morfeusz/20191229/Windows/64/morfeusz2-0.4.0-py3.7-win-amd64.egg
easy_install ścieżka/do/morfeusz2-0.4.0-py3.7-win-amd64.egg
-----------------------------------

WykopPostPrediction is an app for predicting if your posts has the chance to get into "hot" on Wykop's Mikroblog.
"Hot" are top 150 posts in past 24 hours.

Our app works in that way:
1. Scrape data from the site(posts content) for some longer time(at least few days)
2. Clean and normalize data
3. Train models and check accuracy based on used words and hashtags
4. Pick model and classifier and safe predict_proba(probability of prediction)
   for words and hashtags in dataframe
5. Having Predict_proba use probabilities of post words, probabilities of post
   hashtags, number of post words in post and number of post hashtags to make a
   final prediction if post will get to "Hot" using DecisionTreeClassifier.


Post prediction is getting best results using Count vectorizer
with RandomForestClassifier, which is around 0.81.

Post predictions is getting worst results with Count Vectorizer with Multinomial
Naive Bayes classifier, which is around 0.74.

There were few problems with our project. First of all - data gathering.
Due to wykop.pl limitations we only could scrape first 20 pages of mikroblog. Due to that limitation we could only scrape 300 posts daily. That is not the only problem there. 20 pages we could scrape were all top 300 posts in past 24 hours. We couldn't just make our model learn only based on good data, so we assumed that "hot" is only first 150 posts(first 10 pages), and second 150 are not, so everyday we get 150 positive posts and 150 negative posts. That's quite troublesome, because while it is true that first 150 posts are top, second 150 posts were also very popular and had high chance of getting to hot, so we think that accuracy of our model is strongly affected by that problem and it could be better if we could have more variety of posts data.

Also at the beggining of 2020 year wykop had many maintenences and was going through some changes, which resulted in some corrupted data we gathered before, so we had to make some changes in our scraper and get new portion of data, which resulted in relatively small amount of data(around 2500 posts).
That also affected model we chose for final post prediction. Because previously we were working on corrupted data, models showed that count vectorizer gives better results than TFIDF model, which later turned out to not be entirely true. It isn't such a big problem though, because differences between models were very minor.



Our project consists of:
1. Web scraper - for scraping training and test data from mikroblog to csvData.csv file.
   To scrape data from past 24h use command:
   python scrape_data.py
   In scrape_data.py you can precise which pages of mikroblog you want to scrape,
   by passing int arguments(from 1 to 20) of starting page and ending page.

2. ModelPredictionTFIDF - Class that predicts data using Term Frequency,
   Inverse Document Frequency. When creating that class instance you can pass
   classifier and ngrams, so you can test TFIDF with almost every classifier.
   Unfortunately, ModelPredictionTFIDF is made only for classifiers accuracy testing
   with TFIDF method. Due to lower accuracy than CountVector method we haven't made
   it possible to predict post given from user.
   If you want to check actual classifiers accuracy with TFIDF method use command:
   python testing_models_accuracy.py

3. PostNormalizing - class that normalizes and cleans given post data.

4. CountVectorPrediction - Class that predicts data using Count Vectorizer.
   When creating that class instance you can pass classifier, so you can test
   many classifiers with that method. We chose this method as our post prediction
   method because primarly it achieved slightly higher accuracy(although
   it really depends on scraped data and every new data may change it).

5. TreeFinalPrediction - Class that predicts if given post will get to "Hot"
   using prediction_proba of words, hastags, as well as number of words and hashtags
   in given post. Use command: python main.py

6. TestingFunctions - class for unit testing

7. stringFunctions - file with functions, mostly for lemmatizing, normalizing and cleaning.

8. testing_countvect - file with function for testing count vectorizer model
