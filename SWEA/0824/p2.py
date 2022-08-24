def bfs(v, N):
    visited = [0] * (N + 1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v)
        for w in lst[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

P, L = map(int, input().split())
num = list(map(int, input().split()))
lst = [[] for _ in range(P + 1)]
for i in range(0, L * 2, 2):
    lst[num[i]].append(num[i + 1])
    lst[num[i + 1]].append(num[i])
print(lst)

bfs(1, P)