import sys
input = sys.stdin.readline
def f(x,y):
    global ans
    q = [(x,y)]
    visited = [[0]*(W+2) for _ in range(H+2)]
    visited[x][y] = 1
    ans  = 0
    dd = [(0,1),(1,0),(0,-1),(-1,0)]
    q2 = []
    while q:
        x,y = q.pop(0)
        for d in dd:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < H+2 and 0 <= ny < W+2 and visited[nx][ny] == 0 and ddang[nx][ny] != '*':
                if ddang[nx][ny] == '.':
                    visited[nx][ny] = 1
                    q.append((nx,ny))  
                elif 65 <= ord(ddang[nx][ny]) <= 90:
                    if chr(ord(ddang[nx][ny])+32) in key:
                        visited[nx][ny] = 1
                        ddang[nx][ny] = '.'
                        q.append((nx,ny))
                    else:
                        q2.append((x,y))                  #못갔던 곳은 nx,ny로 안넣고 x,y로 넣기!
                elif 97 <= ord(ddang[nx][ny]) <= 122:
                    key.append(ddang[nx][ny])
                    ddang[nx][ny] = '.'
                    visited = [[0]*(W+2) for _ in range(H+2)]
                    q = [(nx,ny)] + q2
                    q2 =[]
                elif ddang[nx][ny] == '$':
                    visited[nx][ny] = 1
                    ddang[nx][ny] = '.'
                    q.append((nx,ny))
                    ans += 1

T = int(input().strip())
for t in range(T):
    H, W = map(int, input().split())
    ddang = [] 
    ddang.append(['.']*(W+2))
    for h in range(H):
        ddang.append(['.']+list(input().strip())+['.'])
    ddang.append(['.']*(W+2))
    key = list(input().strip())

    for a in range(H):
        for b in range(W):
            if chr(ord(ddang[a][b])+32) in key:
                ddang[a][b] = '.'
    f(0,0)
    print(ans)

    # ord chr 65~90 97~122