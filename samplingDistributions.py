import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import pandas as pd
import statistics
import random

df = pd.read_csv('data5.csv')
data = df['temp'].tolist()

dataSet = []
populationMean = statistics.mean(data)
populationStandardDeviation = statistics.stdev(data)
print (populationMean, populationStandardDeviation)
#for i in range (0,100):
#    randomIndex = random.randint(0,len(data))
#    value = data[randomIndex]
#    dataSet.append(value)
#sampleMean = statistics.mean(dataSet)
#sampleStandardDeviation = statistics.stdev(dataSet)

#print (sampleMean ,sampleStandardDeviation)

#fig = ff.create_distplot([dataSet], ['temp'], show_hist = False)
#fig.show()

def randomSetOfMean(counter):
    dataSet = []
    for i in range (0,100):
        randomIndex = random.randint(0,len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)
    sampleMean = statistics.mean(dataSet)
    sampleStandardDeviation = statistics.stdev(dataSet)
    return sampleMean
def showFig(meanList):
    data1 = meanList
    mean = statistics.mean(data1)
    fig = ff.create_distplot([data1],['temp'], show_hist = False )
    fig.add_trace(go.Scatter(x = [ mean,mean], y = [0,1], mode = 'lines', name = 'mean'))
    fig.show()
def setup():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)
    showFig(meanList)
    mean = statistics.mean(meanList)
    print (mean)
setup()

def standardDev():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)
    standardDev = statistics.stdev(meanList)
    print (standardDev)
standardDev()
