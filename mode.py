import csv
from collections import Counter
with open('HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newdata = []
for i in range(len(file_data)):
    numb = file_data[i][2]
    newdata.append(float(numb))
n = len(newdata)
data = Counter(newdata)
get_mode = dict(data)
mode = []
mode1 = []
mode2 = []
for a,v in get_mode.items():
    a = float(a)
    if 50<a<60 :
        if v == max(list(data.values())):
            mode.append(a)
    elif 60<a<70 :
        if v == max(list(data.values())):
            mode1.append(a)
    elif 70<a<75 :
        if v == max(list(data.values())):
            mode2.append(a)
print (len(mode), len(mode2), len(mode1))
if len(mode)>len(mode1) and len(mode2):
    print (mode)
elif len(mode1)>len(mode2) and len(mode):
    print (mode1)
    print (True)
elif len(mode2)>len(mode1) and len(mode):
    print (mode2)
