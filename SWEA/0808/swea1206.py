for t in range(10):
    N = int(input())
    gil = list(map(int, input().split()))
    cnt = 0
    for i in range(2,N-1):
        if gil[i] > gil[i-1] and gil[i] > gil[i-2] and gil[i] > gil[i+1] and gil[i] > gil[i+2]:
            cnt += gil[i] - max(gil[i-2],gil[i-1],gil[i+1],gil[i+2])
    print(f'#{t+1} {cnt}')