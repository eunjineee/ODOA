from collections import deque
import sys
input = sys.stdin.readline

def f():
    global ans
    while q:
        (x,y) = q.popleft()
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        for dd in d:
            nx = x + dd[0]
            ny = y + dd[1]
            # print(f'nz={nz} nx={nx} ny={ny}')
            if n > nx >= 0 and m > ny >= 0 and box[nx][ny] == 0:
                # print(f'실행')
                box[nx][ny] = box[x][y] + 1
                q.append((nx,ny))
                ans += 1



m,n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
q = deque()
ans = 0
for x in range(n):
    for y in range(m):
        if box[x][y] == 1:
            q.append((x,y))
f()

answer = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
        elif box[i][j] > answer:
            answer = box[i][j]
print(answer-1) 