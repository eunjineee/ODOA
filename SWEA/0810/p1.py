import sys
sys.stdin = open('p1.txt')

T = int(input())
dn = [-1, 0, 1, 0]
dm = [0, 1, 0, -1]

for t in range(1,T+1):
    asum = 0
    a = int(input())
    nums = [list(map(int,input().split())) for _ in range(a)]
    for n in range(a):
        for m in range(a):
            for d in range(4):
                nn = n + dn[d]
                nm = m + dm[d]
                if 4 >= nn >= 0 and 4 >= nm >= 0:
                    asum += abs(nums[nn][nm]-nums[n][m])
    print(f'#{t} {asum}')