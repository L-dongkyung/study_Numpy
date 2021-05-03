import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

a = np.zeros((2, 3))
# print(a)
# print(a.dtype)

b = np.ones((2, 3))
# print(b)
# print(b.dtype)

c = np.empty((5, 5))
# print(c)
# print(c.dtype)

d = np.random.random((3, 3))
# print(d)
# print(d.dtype)

e = np.arange(0, 50, 5)
# print(e)

f = np.arange(0, 10)
# print(f)

g = np.arange(10)
# print(g)

h = np.linspace(0, 10, 10)
# print(h)
# (h.size)

i = np.linspace(0, 10)
print(i)
print(i.size)

