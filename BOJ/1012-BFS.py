from collections import deque
T = int(input())

def f(y,x):
    q.append((y,x))
    while q:
        (y,x) = q.popleft()
        d =[(0,1),(1,0),(0,-1),(-1,0)]
        for dd in d:
            nx = x + dd[0]
            ny = y + dd[1]
            if n > ny >= 0 and m > nx >= 0 and ddang[ny][nx] == 1:
                ddang[ny][nx] = 0
                q.append((ny,nx))


for t in range(T):
    m,n,k = map(int, input().split())
    ddang = [[0]*(m) for _ in range(n)]
    for kk in range(k):
        a,b = map(int, input().split())
        ddang[b][a] = 1
    q = deque()
    ans = 0
    for j in range(n):    
        for i in range(m):
            if ddang[j][i] == 1:
                f(j,i)
                ans += 1
    print(ans)