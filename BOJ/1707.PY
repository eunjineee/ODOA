K = int(input())

def f():
    
for k in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for e in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

