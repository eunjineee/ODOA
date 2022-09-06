import heapq as h

n, m = map(int, input().split())
box = list(map(int, input().split()))
child = list(map(int, input().split()))
boxH = []

for b in box:
    h.heappush(boxH, -b)

for c in child:
    b = -h.heappop(boxH)
    if b > c:
        h.heappush(boxH, -(b - c))
    elif b == c:
        continue
    else:
        print(0)
        exit()
print(1)