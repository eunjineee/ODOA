n = int(input())

if n < 4:
    dp = [1] * (n+1)
    dp[1] = 0
else:
    dp = [0] * (n+1)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4,n+1):
        temp1 = temp2 = temp3 = n
        if i % 3 == 0:
            temp1 = dp[i//3] + 1
        if i % 2 == 0:
            temp2 = dp[i//2] + 1
        temp3 = dp[i-1] + 1
        dp[i] = min(temp1, temp2, temp3)
print(dp[n])