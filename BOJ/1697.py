from collections import deque
def f(n):
    q = deque([n])
    global ans
    visited[n] = 0
    while q:
        n = q.popleft()
        for i in range(3):
            if i != 2:
                if 0 <= n + d[i] <= (max(N, k)*2 + 1) and visited[n+d[i]] == -1:
                    new_n = n + d[i]
                    q.append(new_n)
                    visited[new_n] = visited[n] + 1
                    if visited[k] != -1:
                        return visited
            else:
                if 0 <= n * d[i] <= (max(N, k)*2 + 1) and visited[n*d[i]] == -1:
                    new_n = n * d[i]
                    q.append(new_n)
                    visited[new_n] = visited[n] + 1
                    if visited[k] != -1:
                        return visited


N, k = map(int, input().split())

d = [ 1, -1, 2]
visited = [-1] * (max(N, k)*2 + 2)
ans = 0

f(N)
print(visited[k])