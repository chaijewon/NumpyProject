import  pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
import csv
"""
file=open('c:\pydata\seoul.csv','r',encoding="cp949")
data=csv.reader(file)
header=next(data)
max_temp=-999
max_date=''
for row in data:
  if row[-1] == '':
     row[-1]=-999
  row[-1]=float(row[-1])
  if max_temp < row[-1] :
      max_date = row[0]
      max_temp = row[-1]
  print(row)
#print(f"가장 기온이 높은 날:{max_date}")
print(f"가장 높은 온도:{max_temp},날짜:{max_date}")
file.close()
"""
"""
 ['2018-03-17', '108', '6.6', '0.5', 14.0]
   날짜          지점   평균기온 최저   최고 
"""
"""
f=open("c:\pydata\seoul.csv")
data=csv.reader(f)
next(data)
result=[]
for row in data :
    if row[-1] != '':
        result.append(float(row[-1]))
print(len(result))

plt.plot(result)
plt.show()
f.close()
"""
"""
s='Hello Python'
print(s.split())
s='1907-10-01'
print(s.split("-")[0])
print(s.split("-")[1])
print(s.split("-")[2]) 
"""
f=open("c:\pydata\seoul.csv")
data=csv.reader(f)
next(data)
hi=[]
low=[]
for row in data :
    if row[-1] !=''  :
        if row[0].split('-')[1]=='04' and row[0].split('-')[2]=='05':
            hi.append(float(row[-1]))
            low.append(float(row[2]))
#print(hi)
#arr=np.array(result)
#print(arr.mean())
plt.plot(hi,'hotpink',label="high")
plt.plot(low,'skyblue',label="low")
plt.legend()
plt.show()
f.close()
