T = int(input())

arr = []
for _ in range(T):
    num = int(input())
    arr.append(num)

arr.sort()
dp = [0] * (T)
for i in range(T):
    dp[i] = max(arr[i]*(T-i), dp[i-1]) 

print(dp[T-1])