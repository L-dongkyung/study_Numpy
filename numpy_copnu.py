import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

a = np.array([2, 4, 6, 8]).reshape(2, 2)
b = np.array([2, 2, 2, 2]).reshape(2, 2)
c = np.arange(10, 130, 10).reshape(3, 4)
d = np.array([1, 2, 3, 4])
e = np.array([1, 2, 3])
f = 5
print(a)
print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# print(a+b)
# print(a-b)
# print(a*b)
print(np.dot(a, b))
# print(a/b)
# print(c)
# print(f)
# print(d)
# print(e)
# print(c+d)
# print(c+e)
# print(f+c)
# print(f*c)
# print(c/f)
# print(c-f)