import sys
sys.stdin = open('p2.txt')

T= int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    n= len(arr)
    cnt = 0
    Ali = []
    for i in range(1, 1 << n):
        A = 0
        for j in range(n):
            if i & (1 << j):
                A += arr[j]
        Ali.append(A)
    if 0 in Ali:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
