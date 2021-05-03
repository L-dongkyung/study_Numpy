import numpy as np
import warnings
import timeit
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(a[0])
# print(a[1])
# print(a[2])

# print(b[0, 0])
# print(b[0, 1])
# print(b[0, 2])
# print(b[1, 0])
# print(b[1, 1])
# print(b[1, 2])

# print(c.ndim)
# print(c)
# print(c[1, 0, 2])

d = np.arange(24).reshape(2, 3, 4)
# print(d)
# print(d.shape)

# print(timeit.timeit('[ i**2 for i in Z]', setup='Z=range(100)'))
# print(timeit.timeit('j**2', setup='import numpy as np; j=np.array(100)'))

e = np.array([1, 2, 3, 4])
# print(e)
e.shape = 1, 4
print(e)
e.shape = 4, 1
print(e)




