# -*- coding: utf-8 -*-
"""predictive_analytics_ia1_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ipdWkZ4uXC48TCtuzq9NeFZI8ZkYhSPv
"""

import pandas as pd

booking_df = pd.read_csv('/content/booking.csv')
booking_df

booking_df.shape

booking_df.dropna(inplace=True)

booking_df.shape

booking_df['type of meal'].value_counts()

booking_df['car parking space'].value_counts()

booking_df['repeated'].value_counts()

booking_df['P-C'].value_counts()

booking_df.columns

booking_df = booking_df.drop(['Booking_ID','date of reservation'],axis=1)
booking_df

from sklearn.preprocessing import LabelEncoder

cols = ['type of meal','room type','market segment type','booking status']

l_encoder = LabelEncoder()

for col in cols:
  booking_df[col] = l_encoder.fit_transform(booking_df[col])

booking_df

from sklearn.preprocessing import StandardScaler
X = booking_df.drop('booking status',axis=1)
y = booking_df['booking status']
# y = pd.DataFrame(y)

scale = StandardScaler(copy=True,with_mean=True,with_std=True)

X = scale.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LogisticRegression

booking_model = LogisticRegression()

booking_model.fit(X_train,y_train)
y_pred = booking_model.predict(X_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test,y_pred)
acc

from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test,y_pred)
conf_matrix

from sklearn.metrics import classification_report

print(classification_report(y_test,y_pred))

