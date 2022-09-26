def dfs(n):
    global ans
    visited[n] = 1
    if len(dic[n]) == 0:
        ans += 1
    for i in dic[n]:
        if visited[i] == 0:
            dfs(i)

n= int(input())
num = list(map(int,input().split()))
hey = int(input())

dic = {_:[] for _ in range(n)}
for i in range(n):
    if num[i] == -1:
        root = i
    if i == hey:
        continue
    elif num[i] != -1:
        dic[num[i]].append(i) 

if root == hey:
    print(0)
else:
    ans = 0
    visited = [0] * n
    dfs(root)
    print(ans)