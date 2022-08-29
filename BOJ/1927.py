import heapq
import sys
n = int(sys.stdin.readline())
heap = []
result = []

for _ in range(n):
    data = int(sys.stdin.readline())
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, data)
        
for data in result:
    print(data)