'''
E.Franco
12/2018
'''

import pandas as pd
import numpy as np

# Models
from sklearn.svm import SVR
from pyramid.arima import auto_arima

# Hyperparameters
from hyperparameters import SVM_PARAMS
from hyperparameters import ARIMA_PARAMS


class ARIMA_SVM():

	def __init__(self):
		'''
		This class represents an ARIMA model fitted on residuals of SVM regressors
		This is a variation of the (ARIMAX) model wherein we instead fit SVM regressor instead of
		a standard linear regression model.
		'''
		self.svm_train_pred = None
		self.resid = None
		self.svm_pred = None
		self.pred_test = None

	def _fit_predict_SVR(self, x_train, y_train, x_test):
		'''
		This method creates prediction for train set of SVR
		and calculates residual between prediction and actual value
		'''
		model = SVR(**SVM_PARAMS)
		model.fit(x_train, y_train)
		self.svm_train_pred = pd.DataFrame(model.predict(x_train), index=y_train.index, columns=['log_price'])
		self.resid = self.svm_train_pred - y_train
		self.pred_test = model.predict(x_test)

	def _fit_predict_ARIMA(self):
		'''
		This method fits an arima model to the residuals of
		prediction and  ands the forecasts to the prediction

		output:
		- forecasted_resid float: the forecasted residuals of our svm by our ARIMA model
		'''
		ts_model = auto_arima(self.resid, **ARIMA_PARAMS)
		ts_model.fit(self.resid)
		forecasted_resid = ts_model.predict(n_periods=1)
		return forecasted_resid



	def fit_predict(self, x_train, y_train,
	                x_test):
		'''
		This method fits an ARIMA model on the residuals of
		our SVM regressor

		args:
		- x_train N-D dataframe
		- y_train N-D dataframe
		- x_test N-D dataframe
		- num_days int: Number of days we want to forecast

		output:
		- pred 1-D dataframe

		'''
		self._fit_predict_SVR(x_train, y_train, x_test)
		forecasted_resid = self._fit_predict_ARIMA()
		forecast = forecasted_resid + self.pred_test
		return forecast




if __name__ == '__main__':

	df = pd.read_csv('./data/stock_sentiment_series.csv')
	df.dropna(axis=0, inplace=True)
	df['log_price'] = np.log(df['Adj Close']) # log prices for numerical stability
	df.set_index('Date')
	df_train = df[:249] 
	df_test = df[249:]

	x_train = df_train[['sentiment']]
	y_train = df_train[['log_price']]
	x_test = df_test[['sentiment']]
	y_test =  df_test[['log_price']]

	model = ARIMA_SVM()
	forecast = model.fit_predict(x_train, y_train, x_test)
	print('Forecasted Closing Stock Price for Apple: {}'.format(np.exp(forecast[0])))