n = int(input())

a = 1
b = 0
for i in range(n):
    aa = bb = 0
    aa += b
    bb += a + b
    a = aa
    b = bb
print(a, b)