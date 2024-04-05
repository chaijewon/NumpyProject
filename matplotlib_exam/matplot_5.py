import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#데이터 분석에 필요한 pandas 와 numpy를 import 시킨다.

df1 = pd.read_csv('C:/pydata/crime.csv',encoding="cp949")
"""
print(df1.head())
print(df1.tail())
print(df1.info())
print(df1.index)
print(df1.columns)

print(df1['범죄대분류'].unique())
print(df1.groupby(['범죄대분류']).count())

df1_group = df1.groupby('범죄대분류').sum()
#print(df1_group)
"""
df1_group = df1.groupby('범죄대분류').sum()
# 범죄대분류별 합계 계산
#df1_group = np.sum(df1.groupby('범죄대분류').sum(), axis=1) # axis=1 은 같은 행별로 계산하는 옵션이다.

# 인덱스 재설정
df1_group = pd.DataFrame(df1_group).reset_index()

# 컬럼명 변경
df1_group.rename(columns = {0:'total'}, inplace = True) # inplace = True: 변경 사항을 바로 적용

# 'total' 기준으로 내림차순 정렬
# df1_group.sort_values(by='total', ascending=False, inplace = True)

print(df1_group)

crime_list = df1_group['범죄대분류'].tolist()
print(crime_list)

# 막대그래프 시각화
import matplotlib.ticker as ticker
plt.figure(figsize = (15,5))
plt.rc('font', family='Malgun Gothic') # 힌글 폰트 지정(맑은 고딕)
plt.title('범죄대분류 건수', fontsize = 18)

sns.set_style('whitegrid') # 그래프 스타일 지정
sns.despine() # 축/테두리 제거
sns.set_context("talk", font_scale=1) # 스케일 크기 조정

barplot = sns.barplot(data=df1_group, x='범죄대분류', y=df1_group[1])
plt.xlabel('범죄대분류', fontsize=14)
plt.ylabel('사건수', fontsize=13)
plt.xticks(fontsize=12, rotation=10)
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}')) # y축 천단위 콤마 표시

# 막대 위에 정수형 건수 표시
for p in barplot.patches:
    barplot.annotate(format(int(p.get_height()), ','),
                     (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center',
                     xytext=(0, 9),
                     textcoords='offset points',
                     fontsize=12,
                     color='black')

#plt.savefig('image/범죄대분류 건수.png')
plt.show()


