from collections import deque

def f(z,x,y):
    global ans
    q.append((z,x,y))
    while q:
        (z,x,y) = q.popleft()
        d = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
        for dd in d:
            nz = z + dd[0]
            nx = x + dd[1]
            ny = y + dd[2]
            # print(f'nz={nz} nx={nx} ny={ny}')
            if h > nz >= 0 and n > nx >= 0 and m > ny >= 0 and box[nz][nx][ny] == 0:
                # print(f'실행')
                box[nz][nx][ny] == 1
                q.append((nz,nx,ny))
                ans += 1


m,n,h = map(int, input().split())
box = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]
q = deque()
ans = 0
for hi in range(h):
    for x in range(n):
        for y in range(m):
            if box[hi][x][y] == 1:
                f(hi,x,y)
                
print(ans)