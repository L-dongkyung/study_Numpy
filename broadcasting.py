import numpy as np

# 규칙 1 랭크(차원,axit)가 다르면 작은 배열 앞에 1을 맞을때까지 추가한다

a =  np.arange(5).reshape(1,1,5)
b = np.array([10,20,30,40,50])
c = a+b
print(c)

# 규칙 2 열이 1인 배열은 크기가 큰 배열의 크기가 맞게 1이 복사된다
x = np.arange(6).reshape(2,3)
y = np.array([[100],[200]])
z = x+y
print(z)
print(x+1000)

# 배열 반복
a = np.arange(48).reshape(4,3,4)  # -- 4개의 3,4 배열으로 출력
for i in a:
    print("배열:")
    print(i)

for i in a.flat:  # -- 배열을 한줄로 늘리고 하나씩 반복
    print(i)

q1 = np.full((3,4), 1.0)
q2 = np.full((3,5), 2.0)
q3 = np.full((2,4), 3.0)

vq = np.vstack((q1,q3))  # -- v버티컬 수직 결합은 열이 맞아야함
print(vq)
hq = np.hstack((q1,q2))  # -- h 수평 결합은 행이 맞아야함
print(hq)

con0q = np.concatenate((q1,q3), axis=0)  # vstack 동일
con1q = np.concatenate((q1,q2), axis=1)  # hstack 동일
