import heapq
import sys
input = sys.stdin.readline
def d(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for node, cst in field[now]:
            cost = dist + cst
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(que, (cost, node))

INF = float('inf')
N, M = map(int,input().split())
k = int(input().rstrip())
distance = [INF]*(N+1)
field = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cs = map(int,input().split())
    field[start].append((end, cs))

d(k)

for a in distance[1:]:
    if a != INF:
        print(a)
    else:
        print('INF')