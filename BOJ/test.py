def bfs(n,di):
    stack.append(n)
    while stack:
        n = stack.pop()
        if n in di.keys():
            for n in di[n]:
                if visited[n] != 1 and n not in stack:
                    stack.append(n)
        if visited[n] == 0:
            visited[n] = 1
            print(n, end=' ')

n,m,v = map(int, input().split())

di = {}
for _ in range(m):
    root, node = map(int, input().split())
    if root not in di.keys():
        di[root] = [node]
    else:
        if node not in di[root]:
            di[root] += [node]
    if node not in di.keys():
        di[node] = [root]
    else:
        if root not in di[node]:
            di[node] += [root]


stack = []
visited = [0]*(n+1)
bfs(v,di)
print()
q = deque()
visited2 = [0]*(n+1)
# dfs(v,di)