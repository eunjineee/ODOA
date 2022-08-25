import sys
sys.stdin = open('1226.txt')
def bfs(N):
    visited = [[0] * N for _ in range(N)]
    queue = []

    for i in range(N):
        for j in range(N):
            if nums[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1

    while queue:
        i, j = queue.pop(0)
        if nums[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if nums[ni][nj] != 1 and visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
    return 0

for _ in range(10):
    t = int(input())
    nums = [list(map(int,list(input()))) for _ in range(16)]
    print(f'#{t} {bfs(16)}')