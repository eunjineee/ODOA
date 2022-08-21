T = int(input())

for t in range(T):
    nums = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for _ in range(2):
        for y in range(9):
            cnt = len(set(nums[y]))
            if cnt != 9:
                ans = 0
                break
        nums = [list(i) for i in zip(*nums)]

    a = 0
    while a != 6:
        hackin = []
        for i in range(3):
            for j in range(3):
                hackin.append(nums[a+i][a+j])
        if len(set(hackin)) != 9:
            ans = 0
        a += 3
    print(f'#{t+1} {ans}')