
import pandas as pd
import numpy as np
import os
from datetime import date
from math import ceil
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

CP_data = pd.read_csv("C:\\Users\\BhagyashreeBaiP\\OneDrive - PRESCIENCE DECISION SOLUTIONS PRIVATE LIMITED\\Desktop\\Prescience_Projects\\Econometrics\\CP_work\\Cross_price_data.csv")

def week_of_month(dt):
    first_day = dt.replace(day=1)
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()
    return int(ceil(adjusted_dom / 7.0))

def prediction(x1, x2, x3, x4):
    x = CP_data[['KC1011', 'KC730', 'KC693', 'KC771']]
    y = CP_data[['Total Quantity(Y)']]

    # Splitting the data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

    # Linear regression
    LR = LinearRegression()
    LR.fit(x_train, y_train)
    y_pred = LR.predict(x_test)
    y_pred[y_pred < 0] = 0

    print("Intercept value of Model is ", LR.intercept_)
    print("Co-efficient Value of Regression Model is : ", LR.coef_)
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print("R^2 Score :          ", metrics.r2_score(y_test, y_pred))

    return LR.coef_


