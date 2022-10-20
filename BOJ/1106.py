import sys

input = sys.stdin.readline
INF = 1e9

k, n = map(int, input().split())
INF = 1e9

dp = [INF]*(k+100)
dp[0] = 0

for _ in range(n):
    w, v = map(int, input().split())
    for j in range(v, k+100):
        dp[j] = min(dp[j-v] + w, dp[j])

print(min(dp[k:]))