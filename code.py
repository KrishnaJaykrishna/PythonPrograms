import pandas as pd
import csv
import plotly.graph_objects as go
df = pd.read_csv('data4.csv')
mean = df.groupby('level')['attempt'].mean()
print (mean)
fig  = go.Figure(go.Bar(x = df.groupby('level')['attempt'].mean(),y = ['level 1', 'level 2', 'level 3', 'level 4'], orientation = 'h'))
fig.show()
