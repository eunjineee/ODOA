from collections import deque
import sys
input = sys.stdin.readline

def f():
    while q:
        (z,x,y) = q.popleft()
        d = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
        for dd in d:
            nz = z + dd[0]
            nx = x + dd[1]
            ny = y + dd[2]
            if h > nz >= 0 and n > nx >= 0 and m > ny >= 0 and box[nz][nx][ny] == 0:
                # print(f'실행')
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append((nz,nx,ny))



m,n,h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for __ in range(h)]
q = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 1:
                q.append((z,x,y))
f()

answer = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 0:
                print(-1)
                exit()
            elif box[k][i][j] > answer:
                answer = box[k][i][j]
print(answer-1) 