from collections import deque

n = int(input())

nums = []

for i in range(n):
    nums.append(list(map(int,input().split())))

visited = [[0]*n for _ in range(n)]


def f():
    q = deque([])
    q.append((0,0))
    dd = [(0,1),(1,0)]
    visited[0][0] = 1

    while q:
        x,y = q.popleft()
        for d in dd:
            nx, ny = x+d[0]*nums[x][y], y+d[1]*nums[x][y]
            if  0 <= nx < n and 0 <= ny < n:
                if nums[nx][ny] != -1:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                else:
                    return 'HaruHaru'
    return 'Hing'

print(f())