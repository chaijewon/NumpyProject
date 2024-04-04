"""
  딕셔너리 (dict)
  => {}
  => 특징 : {key:value} => javascript (JSON) => DJango => React
  => 순서가 없다 (인덱스번호가 없다)
                --------- list , tuple
  => list,tuple : 인덱스번호를 이용해서 찾는다
  => key를 이용해서 찾는다
"""
info={"id":"hong","pwd":"1234","name":"홍길동"}
print(info)
print(info['id'])
print(info['pwd'])
print(info.keys())
print(info.values())
print(info.items())
info.clear()
print(info)