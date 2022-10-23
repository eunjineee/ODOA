# SWEA 5251.최소이동거리

import heapq
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

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    distance = [100000000]*(N+1)
    field = [[]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        start, end, cs = map(int,input().split())
        field[start].append((end, cs))
    
    d(0)
    print(f'#{tc} {distance[N]}')

'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''
'''
#1 2
#2 4
#3 10
'''