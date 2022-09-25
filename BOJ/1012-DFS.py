import sys
sys.setrecursionlimit(10**7)
T = int(input())

def f(y,x):
    ddang[y][x] = 0
    d =[(0,1),(1,0),(0,-1),(-1,0)]
    for dd in d:
        nx = x + dd[0]
        ny = y + dd[1]
        if n > ny >= 0 and m > nx >= 0 and ddang[ny][nx] == 1:
            ddang[ny][nx] = 0
            f(ny,nx)


for t in range(T):
    m,n,k = map(int, input().split())
    ddang = [[0]*(m) for _ in range(n)]
    for kk in range(k):
        a,b = map(int, input().split())
        ddang[b][a] = 1
    
    ans = 0
    for j in range(n):    
        for i in range(m):
            if ddang[j][i] == 1:
                f(j,i)
                ans += 1
    print(ans)