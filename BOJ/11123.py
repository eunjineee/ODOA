import sys
sys.setrecursionlimit(100000000)
# sys.stdin=open('input.txt')

n = int(input())

def yang(x, y):
    visited[y][x] = 1
    for dd in d:
        ny = y + dd[0]
        nx = x + dd[1]
        if w > nx >= 0 and h > ny >= 0:
            if nums[ny][nx] == '#' and visited[ny][nx] == 0:
                yang(nx,ny)

for i in range(n):
    h, w = map(int, input().split())
    nums = [list(input()) for _ in range(h)]
    visited = [[0]*(w+1) for _ in range(h)]
    d = [(0,1),(1,0),(0,-1),(-1, 0)]

    ans = 0
    for y in range(h):
        for x in range(w):
            if nums[y][x] == '#' and visited[y][x] == 0:
                yang(x,y)
                ans += 1
    print(ans)