import matplotlib.pyplot as plt
import random
import csv
"""
result=[]
for i in range(13) :
    result.append(random.randint(1,1000))
print(sorted(result))

plt.boxplot(result)
plt.show()
"""

f=open("c:\\pydata\\seoul.csv")
data=csv.reader(f)
next(data)
"""
month=[[],[],[],[],[],[],
       [],[],[],[],[],[]]
for row in data:
    if row[-1]!='':
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))
plt.boxplot(month)
plt.show()
"""
day=[]
for i in range(31):
    day.append([])
for row in data:
    if row[-1]!='':
        if row[0].split('-')[1]=='08':
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))
plt.style.use('ggplot')
plt.figure(figsize=(10,5),dpi=300)
plt.boxplot(day)
plt.show()