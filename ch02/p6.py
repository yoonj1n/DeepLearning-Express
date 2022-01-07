#page 89- 넘파이 고유값 다루기

import numpy as np

a= np.array([11,11,11,12,13,14,14,15,16,17,17,17])

#np.unique()사용하면 중복되는 요소를 제외한 array를 얻을 수 있다.
b = np.unique(a)
print(b)

#return_index 인수를 사용해서 "고유값의 인덱스"를 얻을 수 있다.
c,index = np.unique(a, return_index=True)
print(index)

#return_counts 인수를 사용해서 "고유값의 빈도수"를 얻을 수 있다.
d,count = np.unique(a, return_counts=True)
print(count)