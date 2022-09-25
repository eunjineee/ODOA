import sys
input = sys.stdin.readline
n = int(input())

dic = {i:[] for i in range(1,n+1)}

for i in range(n-1):
    a, b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

par = [0] * (n+1)
q = [1]
    
while q:
    now = q.pop(0)
    for nextt in dic[now]:
        if par[now] != nextt:
            par[nextt] = now
            q.append(nextt)

for i in range(2,n+1):
    print(par[i])