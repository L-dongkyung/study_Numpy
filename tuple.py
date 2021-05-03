a = (1, 2, 3)
b = (1, 2, 4)
c = (1, 2, 3)

# print(type(a))
# print(type(a[0]))
# print(type(a[1]))
# print(type(a[2]))

# a[0] = -1
# print(a)
# print(a[0:2])

# print(a == b)
# print(a is b)
# print(a == c)
# print(a is c)

d = list(a)
d[0] = -1
e = tuple(d)
# print(e)

f = (1, 'abc', [1, 2, 3])
before_id = id(f[2])
# print(type(f[2]))
f[2].append(4)
# print(f[2])
# print(id(f[2]) == before_id)
# print(f)
# f[2] = 5

g = 1,2
print(g)
x, y = g
print(x, y)





