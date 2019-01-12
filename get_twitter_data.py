from pattern.web import Twitter
import re
import datetime
from textblob import TextBlob
import got3
import pandas as pd
import os

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_sentiment_score():
	s=[]
	dates=[]
	for j in range(1,13):
	    for i in range(1,32):
	        try:
	            tweetCriteria = got3.manager.TweetCriteria().setQuerySearch('tesla company').setSince("2018-0"+ str(j)+ "-0"+ str(i)).setUntil('2018-0' + str(j) + '-0'+ str(i+1)).setMaxTweets(5)
	            day_sentiment = []
	            for k in range(0, 5):
	                try:
	                    tweet = got3.manager.TweetManager.getTweets(tweetCriteria)[k]
	                except:
	                    break
	                _date = tweet.date
	                tweet= clean_tweet(tweet.text)
	                print(tweet)
	                sentiment = TextBlob(tweet).sentiment.polarity
	                print(sentiment)
	#                 print(sentiment)
	                day_sentiment.append(sentiment)
	            avg_daily_sentiment = sum(day_sentiment) / len(day_sentiment)
	            print(avg_daily_sentiment)
	            dates.append(_date)
	            s.append(avg_daily_sentiment)
	        except:
	            break # No 31 in month
	return (s, dates)	

if __name__ == '__main__':
	(sentiment_score, dates) = get_sentiment_score()
	d = {'Date':dates, 'sentiment':sentiment_score}
	df = pd.DataFrame(d)
	if not os.path.exists('./data/'):
	    os.makedirs('./data/')
	df.to_csv('./data/sentiment_series.csv', index=False)

