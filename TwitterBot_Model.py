'''
Edric Franco
12/2018
'''

from twitterscraper import query_tweets
from pattern.web import Twitter
# from utils import clean_tweet

import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from textblob import TextBlob


class Twitter_Sentiment_Bot():

	def __init__(self, ticker='AAPL', begin_date=dt.date(2018,1 ,1), end_date=dt.date(2018, 12, 31)):
		'''
		This class represents a Twitter sentiment analysis model

        Args:
        - ticker string: ticker symbol of stock
        - begin_date datetime: start date we want to scrape
        - end_date datetime: end date we wan_t to scrape

		'''
		self.ticker = ticker
		self.df = pd.DataFrame()
		self.start = begin_date
		self.end = end_date

	def _get_tweet(self, limit=100, lang='english'):

		'''
		This method creates a dataframe consisting of the scraped tweets with the corresponding timestamp

		Args:
        - ticker string: ticker symbol of stock
        - limit int: amount of tweets per day
        - lang string: language of tweet

		'''

		tweets = query_tweets(self.ticker, begindate=begin_date,
		                      enddate = end_date, limit=limit, lang=lang)

		self.df = pd.DataFrame([t.text, t.timestamp] for t in tweets)
		self.df[1] = self.df[1].dt.date

	def _sentiment_score(self):
		'''
		This method adds the sentiment score using TextBlob API	on the dataframe
		'''
		self.df['sentiment'] = self.df[0].apply(lambda x: TextBlob(x).sentiment.polarity)
		self.df.columns=[['Tweet', 'Date', 'sentiment']]
		self.df = self.df[['Date', 'sentiment']]
		self.df.groupby(['Date']).mean()

	def _merge_stock_data(self):
		'''
		This method adds the stock prices to the dataframe
		'''
		df_prices = web.DataReader(self.ticker, 'yahoo', self.start, self.end)
		df_prices.reset_index(inplace=True)
		df_prices = df_prices[['Date', 'Adj Close']]
		self.df.merge(df_prices, on='Date', how='left')
		self.df = df_prices.merge(self.df, on=['Date','Date'])

	def run_all(self, limit=100, lang='english'):
		'''
		This method creates a dataframe with 4 columns,
		Tweets, Date, sentiment score and adjusted closing prices for the ticker selected

		output:
		dataframe consisting of our desired output
		'''
		df = self._get_tweet(limit=limit, lang='english')
		self._sentiment_score()
		self._merge_stock_data()
		return self.df




if __name__ == '__main__':
	ticker='AAPL'
	begin_date=dt.date(2018,1 ,1)
	end_date=dt.date(2018, 12, 31)

	scrap = Twitter_Sentiment_Bot(ticker=ticker,
		                          begin_date=begin_date,
		                          end_date=end_date)

	limit = 100
	lang = 'english'
	df = scrap.run_all(limit=limit,
		               lang=lang)

	if not os.path.exists('./data/'):
	    os.makedirs('./data/')

	df.to_csv('./data/stock_sentiment_series.csv', index=False)