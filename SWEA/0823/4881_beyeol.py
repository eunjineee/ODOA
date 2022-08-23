def choisohwua(y, x):
    global wanryo
    visited[y][x] = True
    if nums[y][x] == 2:
        wanryo = 1
    for u in range(4):
        ny = y + dy[u]
        nx = x + dx[u]
        if nx >= n or nx < 0 or ny >= n or ny < 0 or visited[ny][nx] == True or nums[ny][nx] == 1:
            continue
        else:
            miro(ny,nx)

T = int(input())
for t in range(T):
    n = int(input())
    nums = [list(map(int,list(input()))) for _ in range(n)]

    wanryo = 0
    choisohwua(y, x)
    print(f'#{t+1} {wanryo}')