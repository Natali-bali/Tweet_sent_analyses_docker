import tweepy
from config import Twitter
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import datetime
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

username='ko.natalia.de@gmail.com'
password='1111111'
# client_atlas = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites=true")
client = pymongo.MongoClient("mongodb") #connected to mongo
try:
    client.admin.command('ismaster')
    print('\n########################################\n\Connection to Mongodb Server Established\\n########################################\n')
except ConnectionFailure:
    print('\n###################################\nConnection to Mongodb Server Failed\n###################################\n')

db = client.tweets #created data base tweets
col = db.tweet_data #created collection base tweet_data


auth = tweepy.OAuthHandler(Twitter['consumer_key'], Twitter['consumer_secret'])
auth.set_access_token(Twitter['access_token'], Twitter['access_token_secret'])

api = tweepy.API(auth)

class TwitterListener(StreamListener):
    def on_data(self, data):
        t = json.loads(data)
        dt = t['created_at']
        created = datetime.datetime.strptime(dt, '%a %b %d %H:%M:%S +0000 %Y')
        tweet={"_id": t['id'],
               "created_at": created,
               "username": t['user']['screen_name'],
               "name": t['user']['name'],
               "location": t['user']['location'],
               }
        if t['truncated']:
            tweet['text'] = t['extended_tweet']['full_text']
        else:
            tweet['text'] = t['text']
        col.insert_one(tweet)
        return True

listener = TwitterListener()
stream = Stream(auth, listener, tweet_mode='extended')
stream.filter(track=['Data Analyst', 'Data Scientist',
'DataScience', 'Data Science', 'DataAnalyst', 'DataScientist'], languages=['en'])

# db = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites=true"
