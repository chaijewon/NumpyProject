# 제작자,차명,생산기간(부터),생산기간(까지),리콜개시일,리콜사유
# makes carname start_year end_year recall_start recall
# 연산처리 => 배열 / 행렬 => DataFrame (Table => 행 / 열)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import matplotlib.font_manager as fm


#그래프 레이아웃
import missingno as msno

#WordCloud
from wordcloud import WordCloud,STOPWORDS
# STOPWORDS : 문법적인 조사,형용사 ... 배제하고 저장 => XX적인 ...
# 지정한다 ... (명사형)
# 데이터 읽기
df = pd.read_csv("c:\\pydata\\car_recall.csv",encoding="euc-kr")
# 상위 5개 출력  => df.head()  , df.head(10) , df.tail()
# print(df.head())
#정보 요약
#print(df.info())
#seaborn에 정보 (버전)
print(sns.__version__)
# 결과치 시각화
#한글 처리
#plt.rcParams['font.family']='Malgun Gothic'
#plt.rcParams['axes.unicode_minus']=False
"""
msno.matrix(df)
plt.show()
"""
#isna() 함수 이용
# print(df.isna().sum())
# print(df)
# 1. 중복값을 제거 ===> 전처리기 (데이터 수집 => 중복값을 제거) => duplicated
# keep => first , last , False => 중복된 데이터를 한개만 남기고 나머지 제거
# print(df[df.duplicated(keep=False)])
print("Before",len(df))
#중복제거
df=df.drop_duplicates()
print("After",len(df))
# 데이터 column변경
print(df['생산기간(부터)'])
# 2019-10-28
# 함수 제작
def parse_year(s):
    return int(s[:4]) # 0~3  2019
def parse_month(s):
    return int(s[5:7]) # 5,6 10

def parse_day(s):
    return int(s[8:]) # 날짜

#print(df['생산기간(까지)'])
# df에 column을 추가
df['start_year']=df['생산기간(부터)'].apply(parse_year)
df['start_month']=df['생산기간(부터)'].apply(parse_month)
df['start_day']=df['생산기간(부터)'].apply(parse_day)

df['end_year']=df['생산기간(까지)'].apply(parse_year)
df['end_month']=df['생산기간(까지)'].apply(parse_month)
df['end_day']=df['생산기간(까지)'].apply(parse_day)

df['recall_year']=df['리콜개시일'].apply(parse_year)
df['recall_month']=df['리콜개시일'].apply(parse_month)
df['recall_day']=df['리콜개시일'].apply(parse_day)

#print(df.head(3))
#필요한 column만 사용 => column의 이름 변경
"""
  alter table car_recall add start_year ...
"""
# alter table car_recall drop column 생산기간(부터)
df = (df.drop(columns=['생산기간(부터)','생산기간(까지)','리콜개시일'])
      .rename(columns={"제작자":'makes',"차명":'model',"리콜사유":'case'}))
print(df.head(3))
# 2022년 대상으로 데이터 분석
df=df[df['recall_year']==2022]
print(df)
# 1. 데이터를 읽고 => 컬럼변경(한글=>영문) , 제어
print(df.recall_year.min(),df.recall_year.max())
# 2. 데이터분석
# 1) 제조사별로 리콜 현황
df.groupby('makes').count()['model'].sort_values(ascending=False)
print("================ 제조사별 리콜 현황 ========================")
print(df.groupby('makes').count()['model'].sort_values(ascending=False))
tmp=pd.DataFrame(df.groupby('makes').count()['model'].sort_values(ascending=False)).rename(columns={"model":"count"})
print("================ 제조사별 리콜 현황 변경후 ==================")
print(tmp)
# 그래프 출력
"""
plt.figure(figsize=(20,10)) #margin-left=20 margin-top=10
ax=sns.countplot(x="makes",data=df,palette="Set2",order=tmp.index)
plt.xticks(rotation=270)
plt.show()
"""
# 차량 모델별 리콜 건수 현황
temp=pd.DataFrame(df.groupby('model').count()['start_year'].sort_values(ascending=False)).rename(columns={"start_year":"count"}).head(10)
print(temp)
#차량 종류 상위 50개 => 시각화
tmp=pd.DataFrame(df.groupby('model').count()['makes'].sort_values(ascending=False))
tmp=tmp.rename(columns={"makes":"count"}).iloc[:50]
print(tmp)
"""
plt.figure(figsize=(20,10)) #margin-left=20 margin-top=10
ax=sns.countplot(x="model",data=df[df.model.isin(tmp.index)],palette="Set2",order=tmp.index)
plt.xticks(rotation=270)
plt.show()
"""
# 3) 월별 리콜 현황
tmp=pd.DataFrame(df.groupby("recall_month").count()['start_year'].sort_values(ascending=False))
tmp=tmp.rename(columns={"start_year":"count"})
print(tmp)
#그래프 출력
"""
plt.figure(figsize=(10,5)) #margin-left=20 margin-top=10
ax=sns.countplot(x="recall_month",data=df,palette="Set2")
plt.xticks(rotation=270)
plt.show()
"""
# 생산연도별 리콜
tmp=pd.DataFrame(df.groupby("start_year").count()['model'].sort_values(ascending=False))
tmp=tmp.rename(columns={"model":"count"}).reset_index()
"""
plt.figure(figsize=(10,5)) #margin-left=20 margin-top=10
ax=sns.lineplot(data=tmp,x="start_year",y="count")
plt.show()
"""
# 가장 최근 4분기 (10,11,12) => 리콜 현황
"""
plt.figure(figsize=(10,5)) #margin-left=20 margin-top=10
ax=sns.countplot(x="makes",data=df[df.recall_month.isin([10,11,12])],palette="Set2")
plt.xticks(rotation=270)
plt.show()
"""
# 7월 이후
"""
plt.figure(figsize=(10,5)) #margin-left=20 margin-top=10
ax=sns.countplot(x="start_year",data=df[df.recall_month>=7],palette="Set2")
plt.xticks(rotation=270)
plt.show()
"""

# 데이터마이닝 => 워드클라우드 (단어별 갯수) => MapReduce
# 1. 제거할 단어를 만든다
set(STOPWORDS)
swords=set(["동안","인하여","있는","경우","있습니다","가능성이","차량의",
            "가","에","될","이","인해","수","중",
            "시","또는","있음","의","로","및","있으며","발생할","이로",
            "오류로","해당"])
text=""
for word in df.case.drop_duplicates():
    text+=word
print(text[:100])
font_path = 'C:/Windows/Fonts/NanumGothic.ttf'

wc1=WordCloud(max_font_size=200,background_color="white",width=800,height=800,
              font_path='NanumGothic.ttf',stopwords=swords)
wc1.generate(text)
plt.figure(figsize=(10,8))
plt.imshow(wc1)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()













