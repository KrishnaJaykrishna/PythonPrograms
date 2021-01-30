import plotly.express as px
import csv
with open('TV_Time_Spent.csv') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = 'Size',y = 'Time Spent Watching')
    fig.show()
