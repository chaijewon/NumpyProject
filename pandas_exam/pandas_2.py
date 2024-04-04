"""
  데이터 구조 => Table형식 => CSV
  ---------- DataFrame
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 파일 읽기 => 데이터 조회 => 추가 ,수정 , 삭제 => CRUD
import csv
# empno ename job ....
file=open('c:\pydata\EMP.csv')
emp=csv.reader(file)
#인덱스번호를 이용해서 값을 추출
for i in emp:
    print(i[1]+'의 직위는 '+i[2])
file.close()
"""
  1. 파일 읽기 
  2. 데이터 추출 : marge (join) , groupby  , 조건 검색 ...
                                mean() / sum() 
  => 판다스 시각화 
"""
#소문자 변환
file = open('c:\pydata\EMP.csv')
emp = csv.reader(file)
for i in emp:
    print(i[1].lower())
file.close()
# INITCAP
file = open('c:\pydata\EMP.csv')
emp = csv.reader(file)
for i in emp:
    print(i[1].title())
file.close()
#문자의 길이
file = open('c:\pydata\EMP.csv')
emp = csv.reader(file)
for i in emp:
    print(i[1], '\t', len(i[1]))
file.close()
#문자열 결합
file = open('c:\pydata\EMP.csv')
emp = csv.reader(file)
for i in emp:
    print(f"{i[1]}의 월급은 {i[5]}입니다")
file.close()
"""
  between ~ and  => 데이터프레임['컬럼'].between(값1,값2)
  in             => 데이터플레임['컬럼'].isin([값1,값2...])
  is null        => 데이터플레임['컬럼'].isnull()
  like           => 데이터플레임['컬럼'].apply(lambda x:x[0])
"""

emp=pd.read_csv('c:\pydata\EMP.csv')
print(emp)
#         읽을 컬럼명                     조건문  ==> in연산자
# isin([]) between(값,값)
print(emp[['EMPNO','ENAME','DEPTNO']][emp['DEPTNO'].isin([10,20,30])])
print(emp[['EMPNO','ENAME','SAL']][emp['SAL'].between(1000,3000)])

print(emp[['EMPNO','ENAME','JOB']][emp['JOB'].isin(['CLERK','MANAGER'])])

print(emp)
print(emp[['EMPNO','ENAME','JOB','SAL','COMM']][emp['COMM'].isnull()])

namse=emp[['ENAME']]
print(namse)
values=emp[['SAL']]
print(values)
df=pd.DataFrame({"names":namse,"sals":values})
print(df)
#plt.bar(namse.values.tolist(),values.values.tolist())
#plt.show()