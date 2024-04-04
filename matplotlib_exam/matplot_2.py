# 막대그래프
import matplotlib.pyplot as plt
import numpy as np
"""
수직 
x=np.arange(3)
years=['2022','2023','2024']
values=[100,500,900]
plt.bar(x,values)
plt.xticks(x,years)
plt.show()
"""
#수평
"""
x=np.arange(3)
years=['2022','2023','2024']
values=[100,500,900]
plt.barh(x,values)
plt.xticks(x,years)
plt.show()
"""
"""
np.random.seed(0)
n=50
x=np.random.rand(n)
y=np.random.rand(n)
area=(30*np.random.rand(n))**2 #size
colors=np.random.rand(n) #색상
plt.scatter(x,y,s=area,c=colors,alpha=0.5,cmap='Spectral')
plt.colorbar()
plt.show()
"""
"""
weight=[89,67,45,39,56,45,89,90,34,54,78,68,95,44,66,70,72,70,90,30]
plt.hist(weight,label='bins=10')
plt.hist(weight,bins=30,label='bins=30')
plt.legend()
plt.show()
"""
"""
import pandas as pd
import csv
file=open('c:\pydata\EMP.csv')
emp=csv.reader(file)
print(emp)
for row in emp:
    print(row[5])

names=['홍길동','이순신','심청이','강감찬','김두한']
values=[34,32,16,18,50]
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False
plt.pie(values,labels=names,autopct="%.1f%%")
plt.show()
"""
arr=np.random.standard_normal((30,40))
plt.matshow(arr)
plt.colorbar()
plt.show()
