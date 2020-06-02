# Stock-Price-with-Sentiment-Analysis
Stock Price Predictor Using Random Forest with Sentiment Analysis

# Scripts
- TwitterBot_model.py is a script that scrapes daily tweets for 1 year and computes average sentiment score per day <br />
- arima_svm.py is a script that fits an ARIMA model to the residuals of a SVM regressor
- model_building.ipynb is a jupyter notebook reading the sentiment scores from the previous script and creating a model using it as a feature in predicting the closing stock price

# Dependencies: 
lxml==3.5.0 <br />
pyquery==1.2.10 <br /
sklearn <br />
matplotlib <br />
pandas
