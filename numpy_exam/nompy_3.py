"""
Set => 중복을 허용하지 않는다
       순서가 없는 데이터 구조 (인덱스 번호가 없다) => 인덱싱/슬라이싱
                       [1] , [2:6]
       {}
"""
names={"홍길동","이순신","강감찬","심청이","홍길동"}
print(names)
"""
  union() => 합집합
  intersect() => 교집합
  difference() => 차집합 
"""
#list
nums=[1,2,3,4,5,6,7,7,9,9] #List
print(nums)
nums=set(nums) # list() , set() #HashSet
print(nums)
nums=list(nums)
print(nums)
#튜플형
nums={10,30,40,50,60,49,40,50}
# 튜플 => 집합 = 튜플
"""
  nums=set(nums)
  nums=tuple(nums)
  nums=tuple(set(nums))
"""
nums=tuple(set(nums))
print(nums)

