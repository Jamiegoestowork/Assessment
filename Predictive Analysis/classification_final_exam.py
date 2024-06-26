# -*- coding: utf-8 -*-
"""classification_final_exam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VOl8-0P7FfG3NKGRI7mnzIuah09TznZG
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,r2_score,precision_score,recall_score

df = pd.read_csv('/content/penguins_classification.csv')
df

df.info()

df.describe()

df.shape

df['species'].value_counts()

df['island'].value_counts()

#Duplicates
print(df.shape)
print(df.duplicated().sum())
df=df.drop_duplicates()
print(df.shape)

#missingvalues
print(df.isna().sum())

#nullvalues

for i in df.select_dtypes(include='object'):
  df[i]=df[i].fillna(df[i].mode()[0])
for i in df.select_dtypes(include=['int64','float64']):
  df[i]=df[i].fillna(df[i].mean())

print(df.isna().sum())

# Plot histograms for numerical columns
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column])
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
# Plot bar charts for categorical columns
for column in df.select_dtypes(include=['object']).columns:
    plt.figure(figsize=(10, 5))
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Bar Chart of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

# Generate scatter plots for pairs of numerical variables
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
X = df.drop('species',axis=1)
y = df['species']

scaler = StandardScaler()
X = scaler.fit_transform(X)

#data split and model
#model1 LogisticRegression
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# For more detailed evaluation
print(classification_report(y_test, y_pred))

#model2 #XGBoost

from xgboost import XGBClassifier
model = XGBClassifier(random_state=42)

# Train the classifier on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the classifier's performance
accuracy = accuracy_score(y_test, y_pred)
print("XGBoost Accuracy:", accuracy)