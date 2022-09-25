from collections import deque
def dfs(n,di):
    q.append(n)
    while q:
        n = q.pop()
        if n in di.keys():
            for i in di[n]:
                if visited2[i] != 1:
                    q.append(i)
        if visited2[n] == 0:
            visited2[n] = 1
            print(n, end=' ')

def bfs(n,di):
    stack.append(n)
    while stack:
        # print(stack)
        n = stack.pop(0)
        if n in di.keys():
            sorted_di = sorted(di[n])
            for ne in sorted_di:
                if visited[ne] != 1 and n not in stack:
                    stack.append(ne)
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
        di[root] += [node]
    if node not in di.keys():
        di[node] = [root]
    else:
        di[node] += [root]

print(di)

q = deque()
visited2 = [0]*(n+1)
dfs(v,di)
print()
stack = []
visited = [0]*(n+1)
bfs(v,di)
