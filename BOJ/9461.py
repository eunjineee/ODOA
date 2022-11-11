n = int(input())

for i in range(n):
    nums = [1,1,1]
    a = int(input())
    for j in range(2, a+1):
        nums.append(nums[j-1] + nums[j-2])
    print(nums[a-1])