import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns
emp=pd.read_csv('c:\pydata\EMP.csv')
"""
result=emp.groupby('DEPTNO')['SAL'].mean().reset_index()
print(result)
result.plot.bar(x='DEPTNO',figsize=(8,5))
plt.show()
"""
"""
emp['HIREDATE']=emp['HIREDATE'].str[:4]
sns.barplot(x='DEPTNO',y="SAL",hue='HIREDATE' ,data=emp)
plt.show()
"""
result=emp.groupby('JOB')['SAL'].sum().reset_index()
colors=sns.color_palette()
print(colors)
print(result)
result['SAL'].plot.pie(labels=emp['JOB'],colors=colors,autopct="%0.0f%%")
#plt.plot(list(result.SAL.values),labels=list(result.JOB.values),
#        colors=colors,autopct="%0.0f%%")
plt.show()

