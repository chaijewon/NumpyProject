import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.font_manager as fm
import missingno as msno
from wordcloud import WordCloud,STOPWORDS
#문법적인 성분을 배제하고 따로 저장
set(STOPWORDS)
print(sns.__version__)
#missingno : 결측치가 있는 데이터 프레임 생성

#파일 읽기
df = pd.read_csv("c:\\pydata\\car_recall.csv",encoding="euc-kr")
#상위 5개 출력
print(df.head())
# df.head(10) , df.tail()
# 정보 요약
print(df.info())
#plt.rcParams['font.family']='Malgun Gothic'
#plt.rcParams['axes.unicode_minus']=False
#결측치를 시각화
#msno.matrix(df)
#plt.show()
#isna()함수를 이용해서 결측치 확인
print(df.isna().sum())
#중복값 확인  duplicated
print(df[df.duplicated(keep=False)]) #한개만 남기고 나머지는 제거 => first / last
print("Before",len(df))
df=df.drop_duplicates()
print("After",len(df))
# 기초적인 데이터형 변환
# 제작자,차명,생산기간(부터),생산기간(까지),리콜개시일,리콜사유
def parse_year(s):
    return int(s[:4])
def parse_month(s):
    return int(s[5:7])
def parse_day(s):
    return int(s[8:])

df['start_year']=df['생산기간(부터)'].apply(parse_year)
df['start_month']=df['생산기간(부터)'].apply(parse_month)
df['start_day']=df['생산기간(부터)'].apply(parse_day)

df['end_year']=df['생산기간(까지)'].apply(parse_year)
df['end_month']=df['생산기간(까지)'].apply(parse_month)
df['end_day']=df['생산기간(까지)'].apply(parse_day)

df['recall_year']=df['리콜개시일'].apply(parse_year)
df['recall_month']=df['리콜개시일'].apply(parse_month)
df['recall_day']=df['리콜개시일'].apply(parse_day)

print(df.head(3))
#불필요한 열은 버리고 열이름 변경
df=df.drop(columns=['생산기간(부터)','생산기간(까지)','리콜개시일']).rename(columns={'제작자':'makes','차명':'model','리콜사유':'case'})
print(df.head(3))
#2020년의 데이터만 대상 => 나머지 데이터셋은 삭제
print(df.recall_year.min(),df.recall_year.max())
df=df[df['recall_year']==2022]
print(df)
#제조사별 리콜 현황 출력
df.groupby('makes').count()['model'].sort_values(ascending=False)
print("=========== 제조사별 리콜 현황 출력 =============")
print(df.groupby('makes').count()['model'].sort_values(ascending=False))
tmp=pd.DataFrame(df.groupby('makes').count()['model'].sort_values(ascending=False)).rename(columns={"model":"count"})
#print(df.groupby('makes').count()['model'].sort_values(ascending=False))
"""
plt.figure(figsize=(20,10))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style="darkgrid")
ax=sns.countplot(x="makes",data=df,palette="Set2",order=tmp.index)
plt.xticks(rotation=270)
plt.show()
"""
print(tmp.index)
#차량 모델별 리콜 건수 분포
pd.DataFrame(df.groupby('model').count()['start_year'].sort_values(ascending=False)).rename(columns={"start_year":"count"}).head(10)

#모델 상위 50개 추출
tmp=pd.DataFrame(df.groupby('model').count()['makes'].sort_values(ascending=False))
tmp = tmp.rename(columns={"makes":"count"}).iloc[:50]
#그래프 사이즈 변경
"""
plt.figure(figsize=(10,5))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style="darkgrid")
ax=sns.countplot(x="model",data=df[df.model.isin(tmp.index)],palette="Set2",order=tmp.index)
plt.xticks(rotation=270)
plt.show()
"""

#월별 리콜 현황 분석
tmp=pd.DataFrame(df.groupby('recall_month').count()['start_year'].sort_values(ascending=False)).rename(columns={"start_year":"count"}).head(10)
print(tmp)
"""
plt.figure(figsize=(10,5))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style="darkgrid")
ax=sns.countplot(x="recall_month",data=df,palette="Set2")
plt.xticks(rotation=270)
plt.show()
"""
#생산연도별 리콜
tmp=pd.DataFrame(df.groupby('start_year').count()['model'].sort_values(ascending=False)).rename(columns={"model":"count"}).reset_index()
"""
plt.figure(figsize=(10,5))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style="darkgrid")
ax=sns.lineplot(data=tmp,x="start_year",y="count")
plt.show()
print(tmp)
"""
#2020년 가장 최근 (10,11,12) 제조사별 리콜 현황

print(df[df.recall_month.isin([10,11,12])].head())
"""
plt.figure(figsize=(10,5))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style="darkgrid")
ax=sns.countplot(x="makes",data=df[df.recall_month.isin([10,11,12])],palette="Set2")
plt.xticks(rotation=270)
plt.show()
"""
#2020 => 7~12 생산 개시연도
"""
plt.figure(figsize=(10,5))
sns.set(font="Malgun Gothic",
        rc={"axes.unicode_minus":False},
        style="darkgrid")
ax=sns.countplot(x="start_year",data=df[df.recall_month>=7],palette="Set2")
plt.xticks(rotation=270)
plt.show()
"""
text=""
for c in df.case.drop_duplicates():
    text+=c
print(text[:100])
wc1=WordCloud(max_font_size=200,background_color="white",width=800,height=800)
wc1.generate(text)
plt.figure(figsize=(10,8))
plt.imshow(wc1)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()