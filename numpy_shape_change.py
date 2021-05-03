import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
# print(a.shape)

b = a.ravel()
# print(b)
# print(b.shape)
# print(b.base)
# print(b.base is a)

c = np.arange(12)
# print(c)
# print(c.shape)

d = np.array([1, 2, 3])
# print(d)
# print(d.shape)

d = d[:, np.newaxis]
# print(d)

e = np.array([[1, 2], [3, 4]])
f = np.array([[0, 1], [0, 4]])
# print(e)
# print(f)

g = np.vstack((e, f))
# print(g)

h = np.hstack((e, f))
# print(h)

m = np.concatenate((e, f), axis=0)
# print(m)
n = np.concatenate((e, f), axis=1)
# print(n)

i = np.array([1, 2, 3])
j = np.array([4, 5, 6])
k = np.array([7, 8, 9])

l = np.column_stack((i, j, k))
print(l)






