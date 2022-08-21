# 1 2 3
# 4 5 6
a = [[1, 2, 3], [4, 5, 6]]
a = list(zip(*a))
print(type(a[0]))
# b = [list(i) for i in zip(*a)]
print(a)
print(b)
