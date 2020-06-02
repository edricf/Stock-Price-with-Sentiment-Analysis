'''
E.Franco
12/2018
'''

import pandas as pd
import pandas_datareader.data as web

from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from statsmodels.tsa.arima_model import ARIMA


class ARIMA_SVM():

	def __init__(self):
		'''
		This class represents an ARIMA model fitted on residuals of SVM regressors
		This is a variation of the (ARIMAX) model wherein we instead fit SVM regressor instead of
		a standard linear regression model.
		'''
		self.pred = None
		self.resid = None

	def _predict_SVR(self, x_train, y_train, x_test):
		'''
		This method creates prediction for train set of SVR
		and calculates residual between prediction and actual value
		'''
		model = SVR()
		model.fit(x_train, y_train)
		self.pred = model.predict(x_train)
		self.resid = y_train - self.pred 

	def _predict_ARIMA(self, AR, I, MA):
		'''
		This method fits an arima model to the residuals of
		prediction and  ands the forecasts to the prediction
		'''
		model = ARIMA(self.forecast)
		forecasts = model.forecast()
		self.pred += forecasts

	def fit_predict(self, x_train, y_train, x_test, y_test):
		'''
		This method fits an ARIMA model on the residuals of
		our SVM regressor

		args:
		- x_train N-D dataframe
		- y_train N-D dataframe
		- x_test N-D dataframe
		- y_test N-D dataframe

		output:
		- pred 1-D dataframe

		'''
		self._predict_SVR(x_train, y_train, x_test)
		self._predict_ARIMA(AR, I, MA)
		return self.pred




if __name__ == '__main__':

	df = pd.read_csv('./data/sentiment_series.csv')
    df['Date'].apply(lambda x: pd.datetime(x).dt.date)
	start = datetime.datetime(2018, 1, 1)
	end = datetime.datetime(2018, 12, 31)
	df_prices = web.DataReader(self.ticker, 'yahoo', start, end)
	df_prices.reset_index(inplace=True)
	df_prices=df_prices[['Date', 'Adj Close']]
	data = df_prices.merge(df,on=['Date','Date'])


	df = pd.read_csv('./data/sentiment_series.csv')


	x_train, x_test, y_train, y_test = train_test_split(df)
	print(df)