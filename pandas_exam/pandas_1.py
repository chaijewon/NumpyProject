"""
 데이터 프레임 => table
"""
import numpy as np
import pandas as pd

emp_df=pd.read_csv("c:\pydata\EMP.csv")
print(emp_df)
dept_df=pd.read_csv("c:\pydata\DEPT.csv")
print(dept_df)
#DataFrame Copy
# create table => select empno,ename,job...
#empcp=emp_df[emp_df['DEPTNO']==30]
#print(emp_df['ENAME'])
#print(emp_df['JOB'])
# SELECT empno,ename,job,sal FROM emp WHERE deptno=20
empcp=emp_df[emp_df['DEPTNO']==30][['EMPNO','ENAME','JOB','SAL']].copy()
print(empcp)

list_data=[[8000,'홍길동','MANAGER','7788','24/04/04',900,200,10],
           [8001,'심청이','CLERK','7788','24/04/04',900,200,10]
          ]
df2=pd.DataFrame(data=list_data,columns=emp_df.columns)
print(df2)
#SELECT empno,ename,sal FROM emp
print(emp_df[['EMPNO','ENAME','SAL']])
#SELECT empno,ename,job,hiredate FROM emp
print(emp_df[['EMPNO','ENAME','JOB','HIREDATE']])
#SELECT empno,ename,sal FROM emp WHERE deptno=10
print(emp_df[['EMPNO','ENAME','SAL']][emp_df['DEPTNO']==10])
print(emp_df[emp_df['DEPTNO']==10][['EMPNO','ENAME','SAL']])
#SELECT * FROM emp WHERE deptno=30 and job='SALESMAN'
print(emp_df[(emp_df['DEPTNO']==30) & (emp_df['JOB']=='SALESMAN')])
#SELECT * FROM emp WHERE deptno=30 or job='SALESMAN' ==> |
print(emp_df[(emp_df['DEPTNO']==30) | (emp_df['JOB']=='SALESMAN')])
#SELECT job,deptno from emp where deptno=30 and (job='SALESMAN' OR deptno=10)
print(emp_df[((emp_df['DEPTNO']==30) & (emp_df['JOB']=='SALESMAN'))|(emp_df['DEPTNO']==10)][['JOB','DEPTNO']])
#GROUP BY => count() => value_counts() min() max() sum() mean() std()
"""
  웹 프로그램 => 1년 (자기개발 = AI) => 3년 (이직,대학원)
"""
#SELECT deptno,count() FROM emp group by deptno
print(emp_df.groupby('DEPTNO')['SAL'].mean())
print(emp_df.groupby('DEPTNO')['SAL'].max())
print(emp_df.groupby('DEPTNO')['SAL'].min())
# select min(),max(),sum(),mean() from emp group by deptno
print(emp_df.groupby('DEPTNO')['SAL'].agg(['min','max','sum','mean']))
print(emp_df.groupby('JOB')['SAL'].agg(['min','max','sum','mean']))
#JOIN
# pd.merge(left , right , how='조인 방식' => left , right , outer , inner)
# select * from emp e , dept d where e.deptno=d.deptno
pf_join=pd.merge(emp_df,dept_df,on="DEPTNO",how="inner")
print(pf_join)
#ORDER BY
print(emp_df.sort_values(by=['SAL'],ascending=False))


