#page 86-89 난수생성

import numpy as np

#균일분포난수
'''
난수 생성은 중요하다 -> 데이터 랜덤 분할, 세트 랜덤 섞기 등
균일분포난수 : 균일한 확률 분포에서 난수 생성
'''
#시드 설정
np.random.seed(100)

#5개의 난수 얻기
print(np.random.rand(5))

#난수로 이루어진 배열 생성 = rand(행,열)
a = np.random.rand(5,3)
print(a)

#a-b 범위 내의 난수 생성
a = 10; b =20
print( (b-a)*np.random.rand(5)+a )

#정수 난수 생성 = randint()
#a-b 범위 내 정수 난수 생성
print(np.random.randint(a,b, size=10)) # size = 난수 생성 개수


#정규분포난수
#randn() 사용
print(np.random.randn(5))
print(np.random.randn(5,3))

#normal() 사용
#평균값과 표준편차를 인수로 보낼 수 있다. normal(loc = 평균, scale = 표준편차, size = 배열의 차원)
print(np.random.normal(0,0.1,5)) #평균 0, 표준편차 0.1, 5개

