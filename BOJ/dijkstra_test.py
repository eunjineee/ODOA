from pprint import pprint
import sys
import heapq

def get_distance(x1, y1, x2, y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

INF = sys.maxsize
n, w = map(int, sys.stdin.readline().rstrip().split())
pos = [[0, 0]]
m = float(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    pos.append([x, y])

for i in range(1, n+1):
    for j in range(i+1, n+1):
        dist = get_distance(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
        if dist <= m:
            nodes[i].append([j, dist])
            nodes[j].append([i, dist])

for _ in range(w):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, 0])
    nodes[b].append([a, 0])

pprint(pos)
pprint(nodes)

def Dijkstra():
    distances = [INF for _ in range(n+1)]
    distances[1] = 0
    pq = []
    heapq.heappush(pq, [0, 1])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_node])
    return int(distances[n]*1000)

print(Dijkstra())