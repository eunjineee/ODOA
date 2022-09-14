import heapq
import sys
n = int(sys.stdin.readline())
hp = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a > 0:
        heapq.heappush(hp,(a,a))
    elif a < 0:
        heapq.heappush(hp,(-a,a))
    else:
        if len(hp) != 0:
            print(heapq.heappop(hp)[1])
        else:
            print(0)
