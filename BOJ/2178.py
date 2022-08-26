def mirochoisokan(nums,goal):
    visited = [[0]*M for _ in range(N)]
    queue = []
    i, j = 0, 0
    queue.append((i,j))
    visited[i][j] = 1

    di = [0, 1, -1, 0]
    dj = [1, 0, 0, -1]

    while queue:
        i,j = queue.pop(0)
        if i == goal[0]-1 and j == goal[1]-1:
            return visited[i][j]
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if goal[0] > ni >= 0 and goal[1] > nj >= 0:
                if nums[ni][nj] == 1 and visited[ni][nj] == 0:
                    queue.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1
    return 0

N, M = map(int,input().split())
go = (N, M)
num = [list(map(int,list(input()))) for _ in range(N)]
print(mirochoisokan(num,go))