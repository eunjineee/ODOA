n, distance = map(int,input().split())

dic = {}
for j in range(n):
    dic[j] = []

for _ in range(n-1):
    a, b, c = map(int,input().split())
    dic[a].append((b, c))
    dic[b].append((a, c))

def f(x, y):
    visited = [0]*(n)
    