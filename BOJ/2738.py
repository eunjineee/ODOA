import sys
N, M = map(int,input().split())
n1 = []
n2 = []

for i in range(N):
    n1.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    n2.append(list(map(int,sys.stdin.readline().split())))
to = [[0]*M for _ in range(N)]

for x in range(N):
    for y in range(M):
        to[x][y] = n1[x][y] + n2[x][y]
for i in range(N):
    for j in range(M):
        print(to[i][j],end=' ')
    print()