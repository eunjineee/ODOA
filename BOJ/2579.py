n = int(input())
step = [0] * (n+2)
dp = [0] * (n+2)

for j in range(n):
    step[j] = int(input())
    
dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(step[0]+step[2], step[1]+step[2])

for i in range(3, n):
    dp[i] = max(step[i]+step[i-1]+dp[i-3], step[i]+dp[i-2])

print(dp[n-1])