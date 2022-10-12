import sys
import heapq
from collections import deque
input = sys.stdin.readline

def f(start):
    q = []
    heapq.heappush(q,(start, 0))
    visited[start] = 0
    while q:
        now, time = heapq.heappop(q)
        if visited[now] < time:
            continue
        if now in roaddi.keys() and len(roaddi[now]) != 0:
            for (node, node_time) in roaddi[now]:
                next_time = time + node_time
                if next_time < visited[node]:
                    visited[node] = next_time
                    heapq.heappush(q, (node, next_time))
    return visited[end]

def f2(start):
    q2 = deque([(start, 0)])
    visited2[start] = 0
    while q2:
        (now, time) = q2.popleft()
        if now == end:
            totalans.append(visited2[now])
            visited2[now] = -1
        if now in roaddi.keys() and len(roaddi[now]) != 0:
            for (node, node_time) in roaddi[now]:
                if visited2[node] == -1:
                    visited2[node] = time + node_time
                    q2.append((node, time + node_time))

while True:
    place, road = map(int, input().split())
    if place == 0 and road == 0:
        break
    start, end = map(int, input().split())

    roaddi = {}                           #딕셔너리 앞뒤로 만들기
    roaddiback = {}
    for i in range(place):
        roaddi[i] = []
        roaddiback[i] = []
    for j in range(road):
        U, V, P = map(int, input().split())
        roaddi[U].append((V, P))
        roaddiback[V].append((U, P))

    INF = sys.maxsize
    visited = [INF] * (place + 1)    
    visited2 = [-1] * (place + 1)    
    totalans = []

    base_ans = f(start)
    print(base_ans)
    print(f'f()return : {visited[end]}')
    print(f'f visited:{visited}')
    
    f2(start)
    print(visited2)

    lastans = -1
    if len(totalans) != 0:
        totalans.sort()
        for answer in totalans:
            if answer > base_ans:
                lastans = answer
                break
    
    print(lastans)


