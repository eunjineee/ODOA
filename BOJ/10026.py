from collections import deque

def f1(x, y):
    global ans1
    munja = grid[x][y]
    q = deque([(x,y)])
    visited[x][y] = 1

    dd = [(1,0),(0,1),(-1,0),(0,-1)]
    while q:
        (x, y) = q.popleft()
        for d in dd:
            if n > x + d[0] >= 0 and n > y + d[1] >= 0:
                nx = x + d[0]
                ny = y + d[1]
                if visited[nx][ny] == 0 and grid[nx][ny] == munja:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    ans1 += 1

def f2(x, y):
    global ans2
    munja = grid[x][y]
    if munja == 'R' or munja == 'G':
        munja = 'RG'
    q2 = deque([(x,y)])
    visited2[x][y] = 1

    dd = [(1,0),(0,1),(-1,0),(0,-1)]
    while q2:
        (x, y) = q2.popleft()
        for d in dd:
            if n > x + d[0] >= 0 and n > y + d[1] >= 0:
                nx = x + d[0]
                ny = y + d[1]
                if visited2[nx][ny] == 0 and grid[nx][ny] in munja:
                    visited2[nx][ny] = 1
                    q2.append((nx,ny))
    ans2 += 1


n = int(input())
grid = [list(input()) for _ in range(n)]
visited = [[0]*(n) for __ in range(n)]
visited2 = [[0]*(n) for __ in range(n)]
ans2 = 0
ans1 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            f1(i, j)
        if visited2[i][j] == 0:
            f2(i, j)
            
print(ans1, ans2)