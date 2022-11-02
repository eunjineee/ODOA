T = int(input())

for t in range(T):
    a = int(input())
    nums = [1, 2, 4, 7]
    for _ in range(4, a):
        nums.append(sum(nums[-3:]))
    print(nums[a-1])