import heapq
import sys
input = sys.stdin.readline

def f(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for j in arr[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost,j[0]))

n, d = map(int, input().split())
arr = [[] for _ in range(d+1)]
distance = [10000] * (d+1)

for i in range(d):
    arr[i].append((i+1, 1))

for _ in range(n):
    s, e, l = map(int, input().split())
    if e > d:
        continue
    arr[s].append((e,l))

f(0)
print(distance[d])