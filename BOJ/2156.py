n = int(input())
nums = []
total = [0] * n
for i in range(n):
    nums.append(int(input()))


if n > 2:
    total[0] = nums[0]
    total[1] = nums[0] + nums[1]
    total[2] = max(nums[0]+nums[2], nums[1]+nums[2])
    for j in range(3, n):
        # print(f'1: {total[j-3] + nums[j-1] + nums[j]}')
        # print(f'2: {total[j-2] + nums[j]}')
        # print(f'3: {total[j-4] + nums[j]}')
        total[j] = max(total[j-3] + nums[j-1] + nums[j], total[j-2] + nums[j], total[j-4] + nums[j-1] + nums[j])
elif n == 2:
    total[0] = nums[0]
    total[1] = nums[0] + nums[1]
elif n == 1:
    total[0] = nums[0]

print(max(total))