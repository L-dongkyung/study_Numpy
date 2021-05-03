import copy

a = [1,2,3]
b = [1,2,3]
c = [2,3,1]

# print(type(a))
# print(type(a[0]))
# print(type(a[1]))
# print(type(a[2]))
# print(a == b)
# print(a == c)
# print(a is b)

x = [2,3,1]

d = x
e = copy.copy(x)
f = copy.deepcopy(x)

# print(d)
# print(e)
# print(f)

# d[0] = 100

# print(x)
# print(d)
# print(e)
# print(f)

e[0] = 200
f[0] = 200

# print(x)
# print(d)
# print(e)
# print(f)

y = [['a','b','c'], [1,2,3]]
g = copy.copy(y)

# print(y is g)
# print(y[0] is g[0])
# print(y[1] is g[1])
y[0].append(100)
# print(y)
# print(g)

z = [['a','b','c'], [1,2,3]]
h = copy.deepcopy(z)
# print(z is h)
# print(z[0] is h[0])
# print(z[1] is h[1])
h[0].append(200)
# print(z)
# print(h)

i = [1,2,3,4,5]
# print(i[0])
# print(i[1])
# print(i[2])
# print(i[3])
# print(i[4])
# print(i[-1])
# print(i[-2])

# print(i[0:3])
# print(i[:3])
# print(i[0:-1])
# print(i[:])
# print(i[0:4:2])

j = [4, 5, 6, 7, 9, 10]
# print(j)
j[0] = -1
# print(j)
j[2:5] = [0, 0, 0, 0]
# print(j)

k = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(k)
# print(k[0])
# print(k[1])
# print(k[2])
# (k[0][0])
# print(k[1][0])
# print(k[2][0])

l = [1, 2, 3, 4, 5, 6]
m = l[0:4]
l[0] = -1
# print(l)
# print(m)

n = list(range(1, 10))
print(n)
o = list(range(1, 10, 2))
print(o)

















