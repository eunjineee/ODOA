nums = [1, 1]
n = int(input())

if n > 2:
    for i in range(2,n):
        nums.append(nums[i-2] + nums[i-1])

print(nums[n-1])