import sys
sys.stdin = open('input.txt')

T =int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    top = 0
    bottom = 0
    for i in range(M):
        bottom += num[i]
    for i in range(N-M+1):
        to = 0
        for m in range(M):
            to += num[i+m]
        if top < to:
            top = to
        if bottom > to:
            bottom = to
    total = top - bottom
    print(f'#{t} {total}')