import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

min_gap = 1000000
visited = [False] * n
def dfs(idx,depth):
    global min_gap
    if depth == n//2:
        print(visited)
        start_team = 0
        link_team = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j] :
                    start_team += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link_team += graph[i][j] 
        gap = abs(start_team-link_team)
        if gap <= min_gap:
            min_gap = gap
        return
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            dfs(i+1,depth+1)
            visited[i] = False

dfs(0,0)
print(min_gap)