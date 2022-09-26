from collections import deque

def f(x,y):
    global ans
    q.append((x,y))
    while q:
        (x,y) = q.popleft()
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        for dd in d:
            nx = x + dd[0]
            ny = y + dd[1]
            # print(f'nz={nz} nx={nx} ny={ny}')
            if n > nx >= 0 and m > ny >= 0 and box[nx][ny] == 0:
                # print(f'실행')
                box[nz][nx][ny] == 1
                q.append((nz,nx,ny))
                ans += 1


m,n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
q = deque()
ans = 0
for hi in range(h):
    for x in range(n):
        for y in range(m):
            if box[hi][x][y] == 1:
                f(hi,x,y)
                
print(ans) 