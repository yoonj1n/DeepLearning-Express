#page 72-78 넘파이 활용

import numpy as np

#형상 지정하고 zeros() ones() eye() 사용하기
#zeros -> 0으로 채워진 배열 만듦
print(np.zeros((3,4))) #인자는 배열의 형상이다 (행,열)
#ones -> 1로 채워진 배열
print(np.ones((3,4)))
#eye() -> 대각선만 1로 채워지고 다른부분은 다 0
print(np.eye((3))) # 대각선만 채워야하니깐 n x n의 형태여야한다.


#배열 자료형 지정하기
# 디폴드 값은 float64이다. 자료형 (int64, float64, unicode_(문자열)) 사용가능
x = np.ones(5, dtype = np.int64)
print(x)


#연속되는 값으로 배열 생성하기
#np.arange(시작값, 종료값, 간격)
print(np.arange(1,5))
print(np.arange(0,10,2)) # 종료값은 포함되지 않는다.


#균일한 간격의 값으로 배열 생성하기
#np.linspace(시작값, 종료값, 갯수)
print(np.linspace(2,10,5))
print(np.linspace(10,100,10))


#배열 정렬하기
#np.sort(~) -> ~배열을 정렬한 배열 생성
y = np.array([1,5,8,4,7,6])
print(np.sort(y))


#두개의 배열 합치기
x = np.array([[1,2],[3,4]])
y = np.array([[4,5],[6,7]])
# axis = 합치는 축을 지정한다. 0 = 수직 1 = 수평
print(np.concatenate((x,y),axis = 0))
print(np.concatenate((x,y),axis = 1))


#두개의 배열 수직으로 합치기
#concatenate 또는 vstack 사용
print(np.vstack((x,y)))


#두개의 배열 수평으로 합치기
#concatenate 또는 hstack 사용
print(np.hstack((x,y)))


#배열 형태 바꾸기
#딥러닝에서는 2차원 배열을 input으로 사용, 1차원이 들어오거나 하면 reshape로 바꿔준다
x = np.arange(12)
print(x.reshape(3,4)) #reshape(행,열)
print(x.reshape(4,-1)) #-1을 인수로 전달하면 데이터 개수에 맞춰서 자동으로 배열 형태 결정한다.


#배열 나누기
array = np.arange(30).reshape(-1,10)
print(array)
#3x10의 배열을 3x3 과 3x7 배열 두 개로 나눈다
ar1,ar2 = np.split(array, [3], axis = 1) #axis = 나누는 축을 선책한다 0 = 가로로 자르기 1 = 세로로 자르기
print(ar1)
print(ar2)


#배열에 새로운 축 추가하기
#newaxis 사용하기 -> "차원"이 하나씩 늘어난다
a = np.arange(6)
print(a.shape)
a1 = a[np.newaxis,:]
print(a1)
print(a1.shape)
a2 = a[:,np.newaxis]
print(a2)
print(a2.shape)
#expand_dims() 사용하기 -> 지정 위치에 새 축을 삽입할 수 있다.
b = np.expand_dims(a, axis=1) #1 = 열 늘리기
print(b)
print(b.shape)
c = np.expand_dims(a, axis =0) # 0 = 행늘리기
print(c)
print(c.shape)

