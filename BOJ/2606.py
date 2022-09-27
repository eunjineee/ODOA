def f(n):
    visited[n] = 1
    if n in di.keys():
        for i in di[n]:
            if visited[i] == 0:
                f(i)

n = int(input())
m = int(input())

di = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in di.keys():
        di[a] = [b]
    else:
        di[a].append(b)
    if b not in di.keys():
        di[b] = [a]
    else:
        di[b].append(a)

visited = [0] * (n+1)
f(1)
print(visited.count(1)-1)




'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7

'''