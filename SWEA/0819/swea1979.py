T = int(input())

for t in range(T):
    n, k = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(n)]
    total = []

    for _ in range(2):
        for x in range(n):
            wo = 0
            for y in range(n):
                if nums[x][y] == 1:
                    wo += 1
                else:
                    total.append(wo)
                    wo = 0
            total.append(wo)
        nums = [list(i) for i in zip(*nums)]

    ans = total.count(k)
    print(f'#{t+1} {ans}')