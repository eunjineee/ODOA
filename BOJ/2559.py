import sys
n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
num =[]
num.append(sum(nums[:k]))
for i in range(n-k):
    num.append(num[i]-nums[i]+nums[i+k])
print(max(num))