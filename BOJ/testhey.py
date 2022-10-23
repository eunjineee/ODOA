import sys

n = int(sys.stdin.readline())

min_gap = 1000000
visited = [False] * n
def dfs(idx,depth):
    global min_gap
    if depth == n//2:
        print(visited)
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            dfs(i+1,depth+1)
            visited[i] = False

dfs(0,0)
