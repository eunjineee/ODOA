import sys
n = int(sys.stdin.readline().rstrip())

nums = [int(sys.stdin.readline().rstrip()) for i in range(n)]
nums.sort()

for j in nums:
    print(j)