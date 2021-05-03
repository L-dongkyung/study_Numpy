import numpy as np
import warnings

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

a = np.array([1, 2, 3])
c = np.array([10, 20, 30])
d = []
# print(a)
# print(a.dtype)
# print(len(a))
# print(type(a))
# print(type(a[0]))
# print(type(a[1]))
# print(type(a[2]))
# print(a.ndim)
# print(a.shape)

b = np.array([[1, 2, 3], [4, 5]])
# print(b)
# print(len(b[0]))
# print(len(b[1]))
# print(b[0])
# print(b[1])

# for x, y in zip(a, c):
#     d.append(a + c)
# print(d)

e = a + c
# print(e)

# f = np.array([1, 2, 3], dtype=np.float32)
# print(f)
# print(f.dtype)

g = np.array([[1, 2, 3], [4, 5, 6]])
# print(g.ndim)
# print(g.shape)
# print(g.size)
# print(g.itemsize)
# print(g.data)
# print(g.max())
# print(g.min())
# print(g.sum())
# print(g.mean())

# print(g.sum(axis=0))
print(g.sum(axis=1))
