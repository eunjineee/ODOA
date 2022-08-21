for t in range(10):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(n):
        nums[-1] -= 1
        nums[0] += 1
        nums.sort()
        if nums[-1] == nums[0]:
            break
    print(f'#{t+1} {nums[-1]-nums[0]}')
