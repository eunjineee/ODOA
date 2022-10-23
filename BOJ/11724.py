import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def f(a):
    visited[a] = 1
    if len(di[a]) > 0:
        for d in di[a]:
            if visited[d] == 0:
                f(d)

n, m = map(int,input().split())

di ={}
for x in range(1,n+1):
    di[x] = []
visited = [1] + [0] * (n)

for _ in range(m):
    u, v = map(int, input().split())
    di[u].append(v)
    di[v].append(u)

ans = 0
for i in range(1,n+1):
    if visited[i] == 0:
        f(i)
        ans += 1

print(ans)

