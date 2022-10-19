
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
    # CP_data['Date'] = pd.to_datetime(CP_data['Date'], errors='coerce')
    # CP_data['Month'] = (CP_data['Date'].dt.month)
    # CP_data['Day']=CP_data['Date'].dt.day # Which day it is ?
    # CP_data['weeknum']=CP_data['Date'].dt.week #which week of the year the date belongs to(week of year)[1-52]
    # CP_data['DAY_OF_WEEK'] =CP_data['Date'].dt.dayofweek # which day of week the date belongs too[0-6]
    # CP_data['WOM']=CP_data['Date'].apply(week_of_month) # which week of the month the date belongs too[1-5]
    # CP_data['DOY']= CP_data['Date'].dt.dayofyear# which day of the year the date belongs too [1-365]
    # CP_data['Day_Name']=CP_data['Date'].dt.day_name()# used to get is_weekday;Mon to Friday-1; sat & sun -0

    # CP_data.loc[(CP_data['Day_Name'] == 'Saturday') | (CP_data['Day_Name'] == 'Sunday'), 'is_weekday'] = '1'
    # CP_data.loc[(CP_data['Day_Name'] != 'Saturday') & (CP_data['Day_Name'] != 'Sunday'),'is_weekday'] = '0'

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


