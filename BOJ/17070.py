import sys
input = sys.stdin.readline

def f(x, y, k):
    global ans
    for d in range(3):
        if (k == 0 and d == 1) or (k == 1 and d == 0):
            continue
        if d != 2:
            if n > x + dd[d][0] >= 0 and n > y + dd[d][1] >=0:
                xx = x + dd[d][0]
                yy = y + dd[d][1]
                if nums[xx][yy] == 0:
                    nums[xx][yy] = 2
                    if xx == n-1 and yy == n-1:
                        ans += 1
                    f(xx, yy, d)
                    nums[xx][yy] = 0
        else:
            if n > x + 1 >= 0 and n > y + 1 >=0:
                xx = x + 1
                yy = y + 1
                if nums[xx-1][yy] == 0 and  nums[xx][yy-1] == 0 and nums[xx][yy] == 0:
                    nums[xx-1][yy] = 3
                    nums[xx][yy-1] = 3
                    nums[xx][yy] = 3
                    if xx == n-1 and yy == n-1:
                        ans += 1
                    f(xx, yy, d)
                    nums[xx-1][yy] = 0
                    nums[xx][yy-1] = 0
                    nums[xx][yy] = 0


def f2(x, y, k):
    global ans
    while q:
        (x, y, k) = q.popleft()
        if k != 2:
            nums[x][y] = 2
        else:
            nums[x-1][y] = 3
            nums[x][y-1] = 3
            nums[x][y] = 3

        for d in range(3):
            if (k == 0 and d == 1) or (k == 1 and d == 0):
                continue
            if d != 2:
                if n > x + dd[d][0] >= 0 and n > y + dd[d][1] >=0:
                    xx = x + dd[d][0]
                    yy = y + dd[d][1]
                    if nums[xx][yy] == 0:
                        if xx == n-1 and yy == n-1:
                            ans += 1                      
                        q.append((xx, yy, d))
            else:
                if n > x + 1 >= 0 and n > y + 1 >=0:
                    xx = x + 1
                    yy = y + 1
                    if nums[xx-1][yy] == 0 and  nums[xx][yy-1] == 0 and nums[xx][yy] == 0:
                        if xx == n-1 and yy == n-1:
                            ans += 1
                        q.append((xx, yy, d))

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]
dd = [(0,1),(1,0),(1,1)]

nums[0][0] = 1
nums[0][1] = 1
ans = 0
if nums[n-1][n-1] != 0:
    ans = 0
else:
    f(0,1,0)

print(ans)