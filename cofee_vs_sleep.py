import plotly.express as px
import csv
import numpy as np
def getDataSource(datapath):
    Ice_Cream_Sales = []
    Temperature = []
    with open(datapath) as f :
        csvreader = csv.DictReader(f)
        for row in csvreader:
            Ice_Cream_Sales.append(float(row['Coffee_in_ml']))
            Temperature.append(float(row['sleep']))
    return {'x':Ice_Cream_Sales, 'y': Temperature}
def findCorrelation(datasource):
    Correlation = np.corrcoef(datasource['x'],datasource['y'])
    print(Correlation[0,1])
def main():
    datapath = 'Cofee_Sleep.csv'
    datasource = getDataSource(datapath)
    findCorrelation(datasource)
main()
