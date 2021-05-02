import numpy as np

# 시작값 끝값 까지의 수를 step 으로 나눔 디폴트=50
# a = np.linspace(0,9,50)
# print(a)

# 임의의 수로 배열 초기화
# b = np.random.rand(3,4)
# print(b)

# c = np.random.randn(3, 4)  # 평균 0, 분산1 정규분포
# print(c)

def my_function(z,x,y):
    return x*y+z

d = np.fromfunction(my_function, (2,10,10))
print(d)

print(d.itemsize)  # -- 각 아이템의 바이트 출력

e = np.arange(24)
e = e.reshape(6,4)
# e.shape = (6,4)
print(e)
