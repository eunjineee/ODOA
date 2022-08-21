for t in range(1,11):
    n = int(input())
    nums = [list(input()) for _ in range(100)]
    to = []
    for i in range(100):
        for j in range(100):
            for k in range(0,101-j):
                hey = nums[i][j:j + k]
                if hey[:] == hey[::-1]:
                    to.append(len(hey))

    for i in range(100):
        for j in range(100):
            if i > j:
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]

    for i in range(100):
        for j in range(100):
            for k in range(0,101-j):
                hey = nums[i][j:j + k]
                if hey[:] == hey[::-1]:
                    to.append(len(hey))

    print(f'#{t} {max(to)}')