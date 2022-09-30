from collections import deque
def f(n):
    q = deque([n])
    global ans , answer
    visited[n] = 0
    while q:
        n = q.popleft()
        for i in range(3):
            if i != 2:
                if n + d[i] == k and answer == visited[n] + 1:
                    ans += 1
                    continue
                if 0 <= n + d[i] <= (max(N, k)*2 + 1) and visited[n+d[i]] == -1:
                    new_n = n + d[i]
                    q.append(new_n)
                    if new_n == k and visited[k] == -1:
                        visited[new_n] = visited[n] + 1
                        answer = visited[new_n]
                        ans += 1
                        continue
                    visited[new_n] = visited[n] + 1
                    
            else:
                if n * d[i] == k and answer == visited[n] + 1:
                    ans += 1
                    continue
                if 0 <= n * d[i] <= (max(N, k)*2 + 1) and visited[n*d[i]] == -1:
                    new_n = n * d[i]
                    q.append(new_n)
                    if new_n == k and visited[k] == -1:
                        visited[new_n] = visited[n] + 1
                        answer = visited[new_n]
                        ans += 1
                        continue
                    visited[new_n] = visited[n] + 1

N, k = map(int, input().split())

if N == k:
    print(0)
    print(1)
else:
    d = [1, -1, 2]
    visited = [-1] * (max(N, k)*2 + 2)
    ans = 0
    answer = -1
    f(N)
    print(visited[k])
    print(ans)