import plotly.express as px
import csv
import numpy as np
def getDataSource(datapath):
    Ice_Cream_Sales = []
    Temperature = []
    with open(datapath) as f :
        csvreader = csv.DictReader(f)
        for row in csvreader:
            Ice_Cream_Sales.append(float(row['Ice-Cream']))
            Temperature.append(float(row['Temperature']))
    return {'x':Ice_Cream_Sales, 'y': Temperature}
def findCorrelation(datasource):
    Correlation = np.corrcoef(datasource['x'],datasource['y'])
    print(Correlation[0,1])
def main():
    datapath = 'Ice_cream_temprature.csv'
    datasource = getDataSource(datapath)
    findCorrelation(datasource)
main()
