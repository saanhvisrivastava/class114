# -*- coding: utf-8 -*-
"""class114.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w3YCgIaQT42pW_zXMxMdPK6vjBuu7Exm
"""



import csv
import pandas as pd
import plotly.express as px
import numpy as np

df=pd.read_csv('class114data.csv')

GRE_score=df['GRE Score'].tolist()
chance_admission=df['Admit'].tolist()

fig=px.scatter(x=GRE_score,y=chance_admission)
fig.show()

m=0.009
c=-2.43
y=[]
for x in GRE_score:
  y_value=m*x+c
  y.append(y_value)

fig.update_layout(shapes=[
  dict(
      type='line',
      y0=min(y),y1=max(y),
      x0=min(GRE_score),x1=max(GRE_score)
  )])

fig.show()

GRE_score_array=np.array(GRE_score)
Admit_array=np.array(chance_admission)
m,c=np.polyfit(GRE_score_array,Admit_array,1)
y=[]
for x in GRE_score_array:
  y_value=m*x+c
  y.append(y_value)

fig.update_layout(shapes=[
  dict(
      type='line',
      y0=min(y),y1=max(y),
      x0=min(GRE_score),x1=max(GRE_score)
  )])

fig.show()

print(m,c)