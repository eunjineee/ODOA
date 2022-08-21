T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(n)]
    totaltop = 0

    for x in range(n-m+1):
        for y in range(n-m+1):
            to = 0
            for nn in range(m):
                to += sum(nums[x+nn][y:y+m])
            if totaltop < to:
                totaltop = to
    print(f'#{t+1} {totaltop}')