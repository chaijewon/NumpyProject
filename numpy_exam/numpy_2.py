"""
  분석에 필요한 자료형 => list,dict,tuple,set
  -----------------
    |
  연산처리 => numpy
    |
  분석 => pandas
   |
  시각화 => matplotlib

  2. Tuple
     리스트와 비슷하지만 한번 정해지면 변경할 수 없는 데이터 구조
     => 데이터베이스
     => ()=> 소괄호 (튜플), []=>대괄호 (리스트)

     score=(90) => 일반 정수
     score=(90,) => 튜플형식
     score=90, => 튜플형식 => () 생략이 가능
"""
score1=(90)
score2=(90,)
score3=90,
print(type(score1))
print(type(score2))
print(type(score3))
# 인덱싱 / 슬라이싱
score=(90,78,96,74,45)
#      0  1   2 3  4
print(score[0])
print(score[2:4])
