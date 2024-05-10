# -*- coding: utf-8 -*-
"""Clustering_final_exam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bk39lA0ou25L4Bu9ZNoXlX9BqVeOnqMR
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans


df = pd.read_csv('/content/customer_segmentation.csv')
df

df.info()

df.describe()

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

#Encoding
cols = df.select_dtypes(include='object')
label_encoder = LabelEncoder()
for col in cols:
    df[col] = label_encoder.fit_transform(df[col])

df.head()


#Normalization
X = df.drop(['ID','Dt_Customer'],axis=1)
cols = X.columns
scaler = StandardScaler()
X = scaler.fit_transform(X)

X

#KMeans

X=pd.DataFrame(scaler.fit_transform(X),columns=cols)
kmeans=KMeans(n_clusters=3,init='k-means++')
y_pred=kmeans.fit_predict(X)
df['Cluster']=y_pred
print(kmeans.cluster_centers_)

df1=df[df.Cluster==0]
df2=df[df.Cluster==1]
df3=df[df.Cluster==2]
plt.scatter(df1['Marital_Status'],df1['Income'],color='green')
plt.scatter(df2['Marital_Status'],df2['Income'],color='red')
plt.scatter(df3['Marital_Status'],df3['Income'],color='black')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('AgeGroup')
plt.ylabel('Spend')
plt.legend()
plt.show()

from sklearn.metrics import silhouette_score
sse = []
sil_score=[]
k_nrg=range(1,10)
for k in range(1,10):
   kmeans = KMeans(n_clusters=k)
   kmeans.fit(df)
   sse.append(kmeans.inertia_)
   if k>=2:
    x=silhouette_score(df, kmeans.fit_predict(df))
    sil_score.append(x)
plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(sse)
plt.show()
plt.xlabel('K')
plt.ylabel('Silhouette Score')
plt.plot(range(2,10),sil_score,color='red')
plt.show()