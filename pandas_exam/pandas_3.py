# CSV 읽기 => 인덱스
# CSV에서 데이터 추출
# 시각화
import pandas as pd
import numpy as np
import csv
"""
file=open("c:\pydata\EMP.csv")
csv=csv.reader(file)
for i in csv:
    print(i[1],i[5])
file.close()
"""

file=open("c:\pydata\EMP.csv")
emp=csv.reader(file)
for row in emp:
    print(row)
print("============================")
for i in emp:
    if i[2]=='SALESMAN' and int(i[5])>1000:
        print(i[1],i[5],i[2])
print("============================")
for i in emp:
    print(i[1],'\t',i[1][0])
