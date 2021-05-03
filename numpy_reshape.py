import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

a = np.arange(16)
# print(a)

b = a.reshape(4, 4)
# print(b)
# print(b.shape)
# print(b.base)
# print(b.base is a)

b[0] = -1
# print(b)
# print(a)

c = b.reshape(2, 8).copy()
# print(c)

c[0] = 0
# print(c)
# print(b)
# print(c is b)

d = np.arange(16)
e = d.reshape(8, -1)
# print(e)

f = d.reshape(-1, 8)
# print(f)

g = d.reshape(2, -1, -1)
print(g)



