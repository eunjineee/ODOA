from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n = int(input().rstrip())

for _ in range(n):
    N = int(input())
    minusq = []
    plusq = []
    ans = ''
    for i in range(N):
        k, num = input().split()
        if ans == 'EMPTY':
            continue
        if k == 'I':
            heappush(plusq, int(num))
            heappush(minusq, -int(num))
        else:
            if len(plusq) == 0 or len(minusq) == 0:
                ans = 'EMPTY'
                continue
            if num == '1':
                p = -heappop(minusq)
                if p not in plusq:
                    ans = 'EMPTY'
                    continue
            else:
                p = heappop(plusq)
                if -p not in minusq:
                    ans = 'EMPTY'
                    continue
    if ans == 'EMPTY':
        print(ans)
    else:
        ma = -heappop(minusq)
        mi = heappop(plusq)
        print(ma, mi)