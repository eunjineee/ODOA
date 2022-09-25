n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums,reverse=True)

ans = 0
for i in range(n):
    ans += nums[i] * (i+1)

print(ans)