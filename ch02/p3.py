#page 78-81 넘파이 인덱싱, 슬라이싱

import numpy as np

ages = np.array([18,25,75,13,55])

#인덱스를 사용한 슬라이싱
print(ages[1:3]) #인덱스 1-2까지
print(ages[:2]) #인덱스 0-1까지


#논리적 인덱싱 (logical indexing)
y = ages>20
print(y) #bool형의 넘파이 배열 형성
#실제 사용은 아래와 같이 많이 사용됨
y = ages[ages>20]
print(y)
#여러가지의 조건식 합쳐서 사용 가능하다 = 논리합 연산자 "|", 또는 "&" 사용
y = ages[(ages>20) & (ages<30)]
print(y)


#2차원배열 인덱싱
#a[0][1] = a[0,1]
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[0,2])
print(a[0][2])
#배열 요소 변경
a[0,2] = 12
print(a[0,2])


#2차원배열 슬라이싱
#큰 행렬에서 작은 행렬을 뽑아내는걸로 이해하자
print(a[0:2,1:3])
#하나의 행만 빼기
print(a[1])
#step 지정하기
print(a[::2,::2]) #2개씩 건너뛰면서 설정해준다