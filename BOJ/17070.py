def f():
    visted[0][0] = 1
    visted[0][1] = 1
    for i in [(0,1),(1,0),(1,1)]:
        


n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]
print(nums)
visited = [[0]*n for _ in range(n)]

