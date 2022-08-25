import sys
sys.stdin = open('swea5105.txt')

def bfs(N):
    visited = [[0]*N for _ in range(N)]
    queue = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if nums[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1

    while queue:
        i, j = queue.pop(0)
        if nums[i][j] == 3:
            return visited[i][j]
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if nums[ni][nj] != 1 and visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return 2

T = int(input())

for t in range(T):
    N = int(input())
    nums = [list(map(int,list(input()))) for _ in range(N)]

    print(f'#{t+1} {bfs(N)-2}')