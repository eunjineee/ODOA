from collections import deque

def f(x,y):
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        x = q.popleft()
        if len(dic[x]) != 0:
            for xx in dic[x]:
                if visited[xx[0]] == 0:
                    visited[xx[0]] = visited[x] + xx[1]
                    if xx[0] == y:
                        q = deque()
                    else:
                        q.append(xx[0])

n, m =map(int, input().split())

dic = {}
for i in range(1, n+1):
    dic[i] = []
for j in range(n-1):
    a, b, c = map(int, input().split())
    dic[a].append((b,c))
    dic[b].append((a,c))

for k in range(m):
    d, e = map(int, input().split())
    visited = [0]*(n+1)
    f(d,e)
    print(visited[e])