import sys
input= sys.stdin.readline

n,m = map(int,input().split())
namu = list(map(int, input().split()))
start, end = 1, max(namu)

namu.sort()

while start <= end:
    mid = (start+end) //2
    total = 0
    for i in namu:
        if i > mid:
            total += (i-mid)
    if total > m:
        start = mid + 1
    elif total < m:
        end = mid- 1
    else:
        print(mid)
        exit()
print(end)