#page 81 넘파이 연산

import numpy as np

#얕은 복사와 깊은 복사
'''
얕은 복사 : 슬라이싱, 인덱싱 연산자는 뷰(view)를 제공한다. 즉, 참조해서 가져오는거임
            그 말은 즉 a라는 넘파이 배열을 b라고 슬라이싱이나 인덱싱으로 들고왔을 때,
            b의 요소를 변경하면 a도 변경된다.
            변경이 되지 않게하려면 깊은 복사가 필요하다.

깊은 복사 : 새로운 넘파이 배열을 제적한다. 이렇게 사용하면 b 요소를 변경해도 a가 변경되지 않는다.
            방법은 a.copy()
'''
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b = a[0] #슬라이싱으로 복사, 얕은복사
print(b)
b[0] = 77 #b의 요소 변경
print(b)
print(a) #a의 요소도 변경된다.

b2 = a.copy() #copy() 깊은복사
print(b2)
b2[0][0] = 1 #b2의 요소 변경
print(b2)
print(a) #a의 요소는 변경되지 않는다.


#배열간 연산
'''
넘파이 배열은 배열 연산이 가능하다. + * 등
모든 배열 연산은 "요소별로 적용된다"
배열연산이 되면, 결과값으로 채워진 "새로운 넘파이 배열을 생성"한다.
'''
ar1 = np.array([[1,2],[3,4],[5,6]])
ar2 = np.array([[1,1],[2,2],[3,3]])
sum = ar1+ar2 # + 연산자 적용
print(sum)
prod = ar1*ar2 # * 연산자 적용
print(prod)
# 제곱도 가능하다
a =np.arange(5)
print(a)
print(a**2)


#배열 내 요소 연산
#sum, min, max, square, mean 등이 있다.
print(ar1.sum()) #ar1 배열 내 모든 요소의 합
print(ar1.min()) #ar1 배열 내 최솟값
print(ar1.max()) #ar1 배열 내 최댓값
print(np.square(ar1)) #ar1 배열 내 요소들 제곱
'''
배열 내 계산을 할땐 배열의 형태를 무시하고 "모든 요소"를 사용한다.
axis 를 사용하면 열, 행 지정해서 열에대한, 행에대한 요소를 계산할 수 있다.
'''
score = np.array([[99,93,60],[68,41,22],[99,89,77],[55,58,78]])
print(score.shape)
print(score.mean()) # 모든 요소에 대한 평균 계산
print(score.mean(axis = 0)) #axis = 축 지정, 0 = 한 열에대한 모든 행의 평균 1 = 한 행에대한 모든 열의 평균
print(score.mean(axis = 1))


#브로드캐스팅(broadcasting)
'''
배열(벡터) * 정수(스칼라) 같은 경우, numpy는 자동으로 스칼라를 적절한 벡터로 변경하여 연산한다.
-> 브로드캐스팅
'''
miles = np.arange(1,4)
result = miles * 1.6
print(result)


#배열 내적
# @ or dot() 사용해야한다. * 사용시 요소간의 곱셈 연산
ar3 =np.array([[1,2,3],[4,5,6],[7,8,9]]) # 3x3 @ 3x2
print(ar3 @ ar2)
print(ar3.dot(ar2))


#배열에 함수 적용
# np 배열에 함수를 적용하면 모든 요소에 적용된다.
b = np.arange(5)
print(10*np.sin(b))

#ssh test