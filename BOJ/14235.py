import heapq
import sys
n = int(sys.stdin.readline())
heap = []
result = []

for _ in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    if data[0] == 0:
        if len(heap) != 0:
            a = -heapq.heappop(heap)
            print(a)
        else:
            print(-1)
    else:
        for i in range(data[0]):
            heapq.heappush(heap, -data[i+1])