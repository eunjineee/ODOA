import sys
input = sys.stdin.readline

def c(a, b):
    global ans
    if b == 0:
        start = 0
        # print(p)
        for i in range(n):
            for j in range(n):
                if i in p and j in p:
                    start += nums[i][j]
                    # print(f'+:{i}{j}{start}')
                elif (i not in p) and (j not in p):
                    start -= nums[i][j]
                    # print(f'-:{i}{j}{start}')
        # print(f'start:{start}')
        if abs(start) <= ans:
            ans = abs(start)
    elif a < b:
        return
    else:
        p[b-1] = arr[a-1]
        c(a-1, b-1)
        c(a-1, b)      


n =  int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

p = [0] * (n//2)
ans = float("inf")
arr = [x for x in range(n)]
c(n, n//2)
print(ans)