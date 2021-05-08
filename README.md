# Tweet_sent_analyses_docker
A Dockerized Data Pipeline that analyzes the sentiment of tweets.

In this project i built a data pippeline that collect tweets and stores them in a database. Next, the sentiment of tweets is analyzed and the annotated tweets are stored in a second database.
I have 2 algoritms for sentimental analys placed in a class sentAnalysis, simple one with dict. of positive or negative words, the second one is vaderSentiment packege SentimentIntensityAnalyzer method.

