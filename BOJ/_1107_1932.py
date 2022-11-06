n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
a = nums[1].index(max(nums[1]))
print(nums)
num = nums[0][0] + max(nums[1])

for i in range(1,n):
    for j in range(len(nums[i])-1):
        
    num += max(nums[i][a], nums[i][a+1])
    a = nums[i].index(max(nums[i][a], nums[i][a+1]))
 
print(num)