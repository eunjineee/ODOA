from collections import deque


def f(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x in dic.keys() and len(dic[x][2]) != 0:
            for k in dic[x][2]:
                if visited[k] == 0:
                    visited[k] = visited[x]+1
                    q.append(k)
    

n = int(input())

dic = {}
for j in range(n-1):
    a, b = map(int, input().split())
    if a in dic.keys():
        dic[a][2].append(b)
        dic[a][0] += 1
    else:
        dic[a] = [1,a,[b]]

print(dic)
num = int(input())
visited = [0]*n
f(0)
print(visited)
print(max(visited))
deep = max(visited)

if deep > num:
    li = dict(sorted(dic.items(), key=lambda item: item[1]))
    print(li)
    # while True:
         
