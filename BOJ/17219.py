n, m = map(int, input().split())

di = {}
for i in range(n):
    a, b = input().split()
    di[a] = b

for j in range(m):
    x = input()
    print(di[x])