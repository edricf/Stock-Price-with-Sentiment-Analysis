---
title: "arima_model"
output:
  html_document:
    keep_md: true
---


```r
setwd('/Users/Edric/Desktop/all/github/first')
library(tidyverse)
```

```
## -- Attaching packages ----------------------------------------------------------------------- tidyverse 1.2.1 --
```

```
## v ggplot2 3.2.1     v purrr   0.3.3
## v tibble  2.1.3     v dplyr   0.8.3
## v tidyr   1.0.0     v stringr 1.4.0
## v readr   1.3.1     v forcats 0.4.0
```

```
## -- Conflicts -------------------------------------------------------------------------- tidyverse_conflicts() --
## x dplyr::filter() masks stats::filter()
## x dplyr::lag()    masks stats::lag()
```

```r
library(forecast)
```

```
## Registered S3 method overwritten by 'xts':
##   method     from
##   as.zoo.xts zoo
```

```
## Registered S3 method overwritten by 'quantmod':
##   method            from
##   as.zoo.data.frame zoo
```

```
## Registered S3 methods overwritten by 'forecast':
##   method             from    
##   fitted.fracdiff    fracdiff
##   residuals.fracdiff fracdiff
```

```r
data <- read.csv('./data/time_series.csv')
data$Date <- as.Date(data$Date)
              
endo_var <- ts(data$sentiment, frequency=365)
prices <- ts(data$Adj.Close, frequency = 365)
par(mfrow=c(2,2))
plot(endo_var)
plot(prices)
acf(diff(prices), lag.max=50)
pacf(diff(prices))
```

![](arima_model_files/figure-html/unnamed-chunk-1-1.png)<!-- -->



```r
endo_var.train <- endo_var[1:200]
prices.train <- prices[1:200]
endo_var.test <- endo_var[201:length(endo_var)]
prices.test <- endo_var[201:length(prices)]
model <- auto.arima(prices.train, xreg=endo_var.train)
preds <- forecast(model, h=42,xreg=endo_var.test)
plot(preds)
```

![](arima_model_files/figure-html/unnamed-chunk-2-1.png)<!-- -->
