
SVM_PARAMS = {
	'kernel':'rbf',
	'degree':3,
	'coef0':0.0,
	'tol':0.001,
	'C':1.0,
	'epsilon':0.1,
	'shrinking':True,
	'cache_size':200,
	'verbose':False,
	'max_iter':-1
}


ARIMA_PARAMS = {
	'start_p':1,
	'start_q':1,
	'max_p':3,
	'max_q':3,
	'm':12,
	'start_P':0,
	'seasonal':True,
	'd':1,
	'D':1,
	'trace':True,
	'error_action':'ignore',  
	'suppress_warnings':True, 
	'stepwise':True
}