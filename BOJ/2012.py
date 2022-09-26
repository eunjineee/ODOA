import sys
input = sys.stdin.readline
n = int(input())

nums = [int(input()) for _ in range(n)]
nums.sort()

ans = 0
for i in range(1,n+1):
    ans += abs(i-nums[i-1])

print(ans)