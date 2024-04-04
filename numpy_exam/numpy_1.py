"""
   자료형
   => 리스트 => []
   => 튜플 => ()
   => 딕트 => {"키":"값"}
   => 데이터 프레임 : table
   => 시리즈 => 일차원 배열
   import numpy as np
   import pandas as pd
   import seaborn as sns
"""
"""
  1. 리스트 자료형 
     = 여러개의 값을 하나의 단위로 묶어주는 자료형 => 배열 
     = 형식 [1,2,3,4,5]
     = 데이터 관리시 효율적으로 관리하기 위해 사용 
       = 접근이 쉽고 수정이 가능 
"""
score = [90, 89, 78, 50, 56]
print(score)
for jumsu in score:
    print(jumsu)
hap = sum(score)
print(f"hap={hap}")
# 리스트인덱싱 => 리스트에 특정 값을 찾는 경우 => 인덱스
#            0   1  2
score = [80,[90,100,85],75,93]
#        0     1         2 3
# 인덱싱
print(score[2])
print(score[3])
print(score[1][1])
# 리스트슬라이싱 : 특정 범위의 요소를 추출
member=["홍길동",90,"심청이",85,"박문수",77,"이순신",99,"강감찬",67]
print(member[0:2])
print(member[4:6])
print(member[2:])
print(member[:])
# 한개 => 인덱스 (0번부터...) , 범위 ==> :
# 요소 변경 / 추가 / 삭제
nums = list(range(10))
print(nums)
# 범위내 요소 변경
nums[2:4]=[20,30]
print(nums)
nums[6:]=[60,70,80,90]
print(nums)
# 데이터 추가 => 크롤링 ==> append
nums.append(50)
print(nums)
nums.append([40,30])
print(nums)

nums.insert(3,200)
print(nums)
# 원하는 위치에 추가 : insert , 뒤에 추가 : append
# 데이터 삭제 => del
nums=[10,20,30,40,50,60,70]
#     0  1  2  3  4  5  6
del nums[3]
print(nums)
# 10 20 30 50 60 70
del nums[3:] # 인덱스번호 3번이후 전체 삭제
print(nums)
# 전체 삭제  => clear
nums.clear()
print(nums)

score=[86,75,56,90,88]
#score.sort()
score.reverse()
print(score)
"""
   sort() , reverse() , del , append() , insert() , clear()
   list=[]
   => ()
   => {}
   => Set
"""


