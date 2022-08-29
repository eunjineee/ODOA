import heapq
import sys
n = int(sys.stdin.readline())
heap = []
result = []

for _ in range(n):
    data = int(sys.stdin.readline())
    if data == 0:
        if len(heap) != 0:
            a = heapq.heappop(heap)[1]
            print(a)
        else:
            print(0)
    else:
        heapq.heappush(heap, (-data, data))