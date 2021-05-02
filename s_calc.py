import numpy as np

# 12개의 0 list 생성
zero = np.zeros(12, dtype=np.float64)  # -- dtype default = float
print(zero)

# 10개의 list 생성
v = np.arange(10, dtype=np.uint64)
print(v)

# v 3배하기
v *= 3
print(v)

# v 평균 구하기
print(v.mean())