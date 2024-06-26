# -*- coding: utf-8 -*-
"""Regression_final_exam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wv_Wdr06b6D9UjVtJP1mBwksyW8b4FiI
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv('/content/Fare prediction.csv')
df

#Duplicates
print(df.shape)
print(df.duplicated().sum())
df=df.drop_duplicates()
print(df.shape)

print(df.isna().sum())

#nullvalues

print(df.isna().sum())

for i in df.select_dtypes(include='object'):
  df[i]=df[i].fillna(df[i].mode()[0])
for i in df.select_dtypes(include=['int64','float64']):
  df[i]=df[i].fillna(df[i].mean())

print(df.isna().sum())

#droppingcolumns
df = df.drop(['key','pickup_datetime'],axis=1)
df.head(2)

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.show()

#Encoding
cols = df.select_dtypes(include='object')
label_encoder = LabelEncoder()
for col in cols:
    df[col] = label_encoder.fit_transform(df[col])

df.head()

#Normalization
X = df.drop('fare_amount',axis=1)
y = df['fare_amount']

scaler = StandardScaler()
X = scaler.fit_transform(X)

#data split and model
#model1 LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse=mean_squared_error(y_test,y_pred)
mae = mean_absolute_error(y_test,y_pred)
me_ae = median_absolute_error(y_test,y_pred)
print(mse,mae,me_ae)

#model2
xgb = XGBRegressor()
xgb.fit(X_train, y_train)
y_pred = xgb.predict(X_test)

mse=mean_squared_error(y_test,y_pred)
mae = mean_absolute_error(y_test,y_pred)
me_ae = median_absolute_error(y_test,y_pred)
print(mse,mae,me_ae)