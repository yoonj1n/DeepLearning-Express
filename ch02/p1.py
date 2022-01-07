#page 69-71 넘파이의 기본
import numpy as np

a = np.array([1,2,3])
print(a)

print(a[0])

b = np.array([[1,1,1],[1,2,3],[74,8,6]])

print(b)

#shape : 배열의 형상, 정수 튜플
print(b.shape)

#ndim : 배열의 차원 개수
print(b.ndim)

#dtype : 요소의 자료형
print(b.dtype)

#itemsize : 요소 하나의 크기 = 요소 자료형의 크기
print(b.itemsize)

#size : 배열 안 전체 요소의 개수
print(b.size)

#####넘파이 배열의 자료형 지정하기
dtype = np.int64 #np 클래스 안에 정의된 상수 이용하기
dtype = "int64" #문자열 사용하기