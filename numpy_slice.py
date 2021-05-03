import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

a = np.array([1, 2, 3])
d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a[0])
# print(a[-1])
# print(a[-2])
# print(d[1, 2])
# print(d[1][2])
# print(d[0])
# print(d[0, :])
# print(d[1])
# print(d[1, :])
# print(d[:, 0])
# print(d[:, 1])
# print(d[..., 0])
# print(d[..., 1])
# print(d[:2, :2])
d[:2, :2] = 0
# print(d)

b = np.arange(9).reshape(3, 3)
# print(b)
# for c in b.flat:
#     print(c)

c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# print(c[0:2])
# print(c[0:2].shape)
# print(c[0:2].ndim)
# print(c[1:2])
# print(c[:])
# print(c[::2])
# print(c[:-2])
# print(c[-2:])
c[0:2] = 100
print(c[:])




