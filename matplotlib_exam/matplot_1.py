"""
 1. pip install matplotlib
 => 데이터는 pandas => 연산처리 numpy
 => 시각화 matplotlib
"""
# 기본 그래프
import matplotlib.pyplot as plt
import pandas as pd
import csv
"""
file=open("c:\pydata\EMP.csv")
emp=csv.reader(file)
data=[]
for i in emp:
    data.append(i[5])
plt.plot(data)
plt.show()
"""
"""
plt.plot([1,2,3,4],[1,4,9,10])
plt.xlabel('ename')
plt.ylabel('sal')
plt.show()
"""
# 축 레벨을 설정
"""
plt.plot([1,2,3,4],[1,4,9,10],label="Price($)")
plt.legend()
plt.show()
"""
# 축 범위 => 암기
"""
plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel('ename')
plt.ylabel('sal')
plt.xlim([0,10]) #1~4 , 1~16 인원수
plt.ylim([0,20]) # 점수 
plt.show()
"""
"""
plt.plot([1,2,3],[4,4,4],'-',color="C0",label="Solid") #default
plt.plot([1,2,3],[3,3,3],'--',color="C0",label="Dashed")
plt.plot([1,2,3],[2,2,2],':',color="C0",label="Dotted")
plt.plot([1,2,3],[1,1,1],'-.',color="C0",label="DashDot")
plt.xlim([0,5])
plt.ylim([0,5])
plt.legend()
plt.show()
"""
# 마커
"""
plt.plot([1,2,3],[5,6,9],'m*--') #default
plt.show()
  color 'b' ,'g' ,'r' .... 'm' 'k' 'w'  'c'
  '-' '--' ':' '-.'  => bo
"""
"""
plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel('이름')
plt.ylabel('급여')
plt.show()
"""
"""
plt.plot([1,2,3,4],[2,3,5,10],'r')
plt.plot([1,2,3,4],[2,4,7,11],'b')
plt.plot([1,2,3,4],[2,5,8,12],'g')
plt.show()
"""
#Full
"""
x=[1,2,3,4]
y=[2,3,5,10]
plt.plot(x,y)
plt.fill_between(x[1:3],y[1:3],alpha=0.5)
plt.show()
"""