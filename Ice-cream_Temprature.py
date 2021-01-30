import plotly.express as px
import csv
with open('Ice_cream_temprature.csv') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = 'Temperature',y = 'Cold drink')
    fig.show()
