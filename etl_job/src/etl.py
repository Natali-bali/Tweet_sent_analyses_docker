import json
import logging
import re
import time
import datetime
from pymongo import MongoClient
from sqlalchemy import create_engine, exc

# Mongo connection
client = MongoClient("mongodb") #connected to mongo
db = client.tweets #created data base tweets
col = db.tweet_data #created collection base tweet_data

# Postgres connection
pg = create_engine('postgres://user:111111@tweet_psql:5432/tweets')
### INSERT A TABLE
pg.execute('''CREATE TABLE IF NOT EXISTS tweets_psql (tweet_id NUMERIC, tweet VARCHAR(5000), neg NUMERIC, neu NUMERIC, pos NUMERIC, compound NUMERIC, sentiment2 NUMERIC);''')
#
time.sleep(10)
date = "Thu Mar 04 15:26:14 +0000 2021"
date = datetime.datetime.strptime(date, '%a %b %d %H:%M:%S +0000 %Y')

def extract(last_time):
    global date
    tweets = db.tweet_data.find({'created_at': {'$gte': last_time}})
    # tweets = db.tweet_data.find()
    logging.critical('extract function')
    result=[]
    try:
        for tweet in tweets:
            result.append([tweet['_id'], tweet['text']])
            date=tweet['created_at']
    except:
        logging.critical('no tweets')
    # logging.critical(f'extract results:{result}')
    return result
def basic_cleaner(text):
    text = re.sub(r'[^\w]', ' ', text).lower()
    return text
    # ' '.join(re.findall('(?u)\\b\\w\\w+\\b',text.lower()))

def transform(tweets):
    logging.critical('transform function')
    logging.critical(date)
    result=[]
    for tweet in tweets:
        t=basic_cleaner(tweet[1])
        sent_score1 = sentAnalysis(t).vander()
        neg = sent_score1['neg']
        neu = sent_score1['neu']
        pos = sent_score1['pos']
        compound = sent_score1['compound']
        sent_score2 = sentAnalysis(t).easy()
        result.append([tweet[0],t,neg,neu,pos,compound,sent_score2])
    return result

def load(id, tweet, neg, neu, pos, compound, sentiment2):
    pg.execute(f"""INSERT INTO tweets_psql VALUES ('{id}','{tweet}','{neg}','{neu}','{pos}','{compound}','{sentiment2}');""")
    logging.critical("tweet + sentiment written to PG")

while True:
    tweets = extract(date)
    if tweets:
        tweets_scores = transform(tweets)
        for tweet_score in tweets_scores:
            load(tweet_score[0], tweet_score[1], tweet_score[2], tweet_score[3],tweet_score[4], tweet_score[5], tweet_score[6])
    else:
        logging.critical('no tweets')
    time.sleep(10)