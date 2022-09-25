def bfs(n):         #큐
    q = [n]
    visited_bfs[n] = 1
    print(n,end=' ')
    while q:
        now_node = q.pop(0)
        for next_node in sorted(dic[now_node]):
            if visited_bfs[next_node] == 0:
                q.append(next_node)
                visited_bfs[next_node] = 1
                print(next_node, end=' ')

def dfs(now_node):   #재귀
    print(now_node, end=' ')
    visited_dfs[now_node] = 1
    for next_node in sorted(dic[now_node]):
        if visited_dfs[next_node] == 0:
            dfs(next_node)


n,m,v = map(int,input().split())

dic = {i: [] for i in range(1, n+1)}

for i in range(m):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)


visited_dfs = [0] * (n+1)
dfs(v)
print()
visited_bfs = [0] * (n+1)
bfs(v)
