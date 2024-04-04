"""
  1. 넘파일의 특징
     = 연산을 위한 라이브러리
     = 행렬/배열 처리
     = 난수 생성

     1) .ndim  => 열수 (차원)
     2) .shape => 배열의 차원
     3) 접근 => print(b[0,0])
"""
import numpy as np
a=[[1,2,3],[4,5,6]]
b=np.array(a)
print(b)
print(b.ndim)  # 2차원
print(b.shape) # 2행 , 3열
# 특수배열
print(np.arange(10)) # 1씩 증가하는 1차원 배열 (시작 0부터)
print(np.arange(5,10)) #1씩 증가 => 5부터 시작
print(np.zeros((2,2))) # 초기화 => 영행렬
print(np.ones((2,3)))
# 슬라이싱
data=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# 3행 3열 배열
arr=np.array(data)
print(arr)
print(arr.shape)
a=arr[0:2,0:2]
print(a)
"""
  산술 연산자 (+,-,*,/)
  => add() +
  => substract() -
  => multiply() *
  => divide() /
"""
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b
print(c)
#c=np.add(a,b)
#print(c)
c=a-b
print(c)

c=a*b
print(c) # 4 , 10 , 18

c=a/b
print(c) # 1/4 , 2/5 , 3/6 => / 실수
# dot() , sum() , mean() , std()
# => 행렬 * , 합  , 평균 , 표준편차
arr1=[[1,2],[3,4]]
arr2=[[5,6],[7,8]]
a=np.array(arr1)
b=np.array(arr2)
c=np.dot(a,b)
print(c)

a=np.array([[-1,2,3],[3,4,8]])
s=np.sum(a)
print(s)
s=np.mean(a) #평균
print(s)
s=np.std(a)
print(s) # 표준 편차
# 배열 / 행렬


