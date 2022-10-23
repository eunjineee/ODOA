import sys
input = sys.stdin.readline

<<<<<<< HEAD
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
=======
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
        
>>>>>>> 2a84d7e9530aaf8c23ec97412a5affe040c2223d


n =  int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

<<<<<<< HEAD
p = [0] * (n//2)
ans = float("inf")
arr = [x for x in range(n)]
c(n, n//2)
=======
arr = [0] * n
ans = float("inf")

f(0,0)
>>>>>>> 2a84d7e9530aaf8c23ec97412a5affe040c2223d
print(ans)