import sys
sys.stdin = open('swea4837.txt')

T = int(input())
a = [x for x in range(1,13)]

for t in range(1, T+1):
    tot = 0
    num, goal = map(int, input().split())
    for i in range(1, 1 << 12):
        cnt = 0
        numsum = 0
        for j in range(12):
            if i & (1 << j):
                numsum += a[j]
                cnt += 1
        if cnt == num and numsum == goal:
            tot += 1

    print(f'#{t} {tot}')