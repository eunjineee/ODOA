a, b = map(int, input().split())
nums = list(map(int,input().split()))

for i in range(len(nums)):
    print(nums[i]-(a*b),end=' ')