from cmath import inf
import heapq
import sys
input = sys.stdin.readline

def f(start):
    q = []
    heapq.heappush(q,(start, 0))
    visited[start] = 0
    while q:
        now, time = heapq.heappop(q)
        if visited[now] < time:
            continue
        if now in di.keys() and len(di[now]) != 0:
            for (node, node_time) in di[now]:
                next_time = time + node_time
                if next_time < visited[node]:
                    visited[node] = next_time
                    heapq.heappush(q, (node, next_time))


T = int(input())

for t in range(1, T+1):
    computer, link, virus = map(int, input().split())
    di = {}
    for _ in range(link):
        a, b, s = map(int, input().split())
        if b not in di:
            di[b] = [(a,s)]
        else:
            di[b].append((a,s))
    
    visited = [float(inf)] * (computer + 1)
    
    f(virus)
    
    ansnum = 0
    anscount = 0
    for j in range(computer+1):
        if visited[j] != inf:
            anscount += 1
            if visited[j] > ansnum:
                ansnum = visited[j]
    print(anscount, ansnum)