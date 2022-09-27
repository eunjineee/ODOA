import sys
input = sys.stdin.readline
n,m = map(int, input().split())
num = list(map(int, input().split()))
dp = [0] *(n+1)

for j in range(n):
    dp[j+1] = dp[j] + num[j]

for i in range(m):
    a, b = map(int, input().split())
    print(dp[b]-dp[a-1])
