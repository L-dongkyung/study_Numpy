import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

a = np.arange(9).reshape(3, 3)
c = np.arange(18).reshape(3, 6)
# print(a)
# print(c)

b = np.hsplit(a, 3)
# print(b)
# print(b[0])
# print(b[1])
# print(b[2])

d = np.hsplit(c, (2, 5))
# d[:, 0:2] d[:, 2:5] d[:, 5,]
# print(c)
# print(d)
# print(d[0])
# print(d[1])
# print(d[2])

e = np.vsplit(a, 3)
# print(e)
# print(e[0])
# print(e[1])
# print(e[2])

# d[:1, :] d[1:4, :] d[:, 5,]
f = np.arange(18).reshape(3, 6)
g = np.vsplit(f, (1, 4))
print(f)
print(g)
print(f[0])
print(f[1])
print(f[2])
