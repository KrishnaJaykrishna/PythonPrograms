import csv
with open('HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newdata = []
for i in range(len(file_data)):
    numb = file_data[i][2]
    newdata.append(float(numb))
n = len(newdata)
total = 0
for x in newdata:
    total = total + x
mean = total/n
print (mean)
