import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics
import random

df = pd.read_csv('data5.csv')
data = df['temp'].tolist()
populationMean = statistics.mean(data)
fig = ff.create_distplot([data], ['temp'], show_hist = False)
fig.show()
