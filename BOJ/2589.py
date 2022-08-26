di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def mirochoisokan(nums,goal,start):
    visited = [[0]*(M+2) for _ in range(N+2)]
    queue = []
    i, j = start
    queue.append((i,j))
    visited[i][j] = 1

    len_max = 0
    while queue:
        i,j = queue.pop(0)
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if goal[0] > ni >= 0 and goal[1] > nj >= 0:
                if nums[ni][nj] == 'L' and visited[ni][nj] == 0:
                    queue.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1
    
    for jj in visited:
        len_max = max(len_max, *jj)
    
    return len_max-1

N, M = map(int,input().split())
go = (N+2, M+2)
bomul = [['W'] + list(input()) + ['W'] for _ in range(N)]
bomul = [['W']*(M+2)] + bomul + [['W']*(M+2)]
total = []

for i in range(1,N+1):
    for j in range(1,M+1):
        if bomul[i][j] == 'L':
            a = 0
            for wuiare in range(4):
                if bomul[i+di[wuiare]][j+dj[wuiare]] == "L":
                    a += 1
            if a >= 3 :
                continue
            start = (i,j)
            total.append(mirochoisokan(bomul,go,start))

print(max(total))