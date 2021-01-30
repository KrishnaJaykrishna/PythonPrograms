import plotly.express as px
import csv
with open('Cofee_Sleep.csv') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = 'Coffee_in_ml',y = 'sleep')
    fig.show()
