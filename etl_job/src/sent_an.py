import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
class sentAnalysis:
    def __init__(self,t):
        self.tweet = t
    def easy(self):
        n=[]
        p=[]
        neg_w = []
        pos_w = []
        with open('/my_code/src/positive-words.txt', 'r') as f:
            for line in f.readlines():
                pos_w.append(line.strip('\n'))
        with open('/my_code/src/negative-words.txt', mode='r', encoding='latin-1') as f:
            for line in f.readlines():
                neg_w.append(line.strip('\n'))
        t = self.tweet
        def check(tweet, neg, pos):
            tweet=tweet.lower().split()
            for word in tweet:
                if word in neg:
                    n.append(word)
                elif word in pos:
                    p.append(word)
            if len(n)>len(p):
                return -1
            elif len(n)<len(p):
                return 1
            else:
                return 0
        result = check(t, neg_w, pos_w)
        return result
    def vander(self):
        t = self.tweet
        s = SentimentIntensityAnalyzer()
        # def basic_cleaner(text):
        #     return ' '.join(re.findall('(?u)\\b\\w\\w+\\b',text.lower()))
        # tweet = basic_cleaner(t)
        return s.polarity_scores(t)
