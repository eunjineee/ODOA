import sys
sys.stdin = open('5102.txt')

def bfs(v,t):
    q = []
    q.append(v)
    visited = [0] * (N)
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in adjlist[v]:
            if w == t:
                return visited[v]
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    N = V + 1
    adjlist = [[] for _ in range(N)]

    for i in range(E):
        a, b = map(int, input().split())
        adjlist[a].append(b)
        adjlist[b].append(a)

    S, G = map(int, input().split())
    print(f'#{t+1} {bfs(S,G)}')
