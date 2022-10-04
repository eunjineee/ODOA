import sys
input = sys.stdin.readline

def f(i,k):
    global ans
    if k == n//2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if arr[i] == 1 and arr[j] == 1:
                    start += nums[i][j]
                elif not arr[i] == 1 and not arr[j] == 1:
                    link += nums[i][j] 
        if abs(start-link) <= ans:
            ans = abs(start-link)
        return
    for u in range(i,n):
        if arr[u] == 0:
            arr[u] = 1
            f(i+1,k+1)
            arr[u] = 0
        


n =  int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

arr = [0] * n
ans = float("inf")

f(0,0)
print(ans)