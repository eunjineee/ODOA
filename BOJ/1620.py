import sys
n, m = map(int, sys.stdin.readline().split())

di = {}
li = [0] * (n+1)
for i in range(1,n+1):
    a = sys.stdin.readline().strip()
    li[i] = a
    di[a] = i

for j in range(m):
    t = sys.stdin.readline().rstrip()
    if t.isdigit():
        print(li[int(t)])
    else:
        print(di[t])