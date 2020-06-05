# Stock-Price-with-Sentiment-Analysis
Stock Price Predictor Using Sentiment Analysis on Tweets as Input to our SVM regressor and using an ARIMA model to forecast the residuals  of our predictions resulting in a more stable forecast

# Scripts
- TwitterBot_model.py is a script that scrapes daily tweets for 1 year and computes average sentiment score per day, it then merges the stock price of the desired ticker <br />
- hyperparameters.py includes the hyperparameters of our SVM and ARIMA model
- arima_svm.py is a script that fits an ARIMA model to the residuals of a SVM regressor
- model_building.ipynb is a jupyter notebook reading the sentiment scores from the previous script and creating a model using it as a feature in predicting the closing stock price
