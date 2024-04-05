import csv
import matplotlib.pyplot as plt
"""
  막대그래프 : bar
  히스토그램 : hist
  원형 : pie 
"""
"""
f=open('c:\\pydata\\seoul.csv')
data=csv.reader(f)
next(data)
result=[]
for row in data:
    month=row[0].split('-')[1]
    if row[-1]!='':
        if month=='04':
          result.append(float(row[-1]))
plt.hist(result,bins=100,color='r')
plt.show()
"""
f=open("c:\\pydata\\seoul.csv")
data=csv.reader(f)
"""
print(data)
for row in data:
    print(row)
#next(data) #header다음
"""
next(data) #타이틀을 제외
a=[]
b=[]
for row in data:
    month=row[0].split('-')[1]
    if row[-1] !='':
        if month=='04':
            a.append(float(row[-1]))
        if month=='05':
            b.append(float(row[-1]))
plt.hist(a,bins=100,color='r',label='4M')
plt.hist(b, bins=100, color='g', label='5M')
plt.legend()
plt.show()
