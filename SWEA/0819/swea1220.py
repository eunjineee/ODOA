for t in range(10):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    nums = list(zip(*nums))
    zz = 0
    cnt = 0
    for j in range(n):
        zz = 0
        for i in nums[j]:
            if i == 1 and zz == 0:
                zz += 1
            elif i == 2 and zz == 1:
                zz = 0
                cnt += 1

    print(f'#{t+1} {cnt}')