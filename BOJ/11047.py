n, k = map(int, input().split())

money = [int(input()) for _ in range(n)]

ans = 0
for i in range(1,n+1):
    if k >= money[-i]:
        ans += k//money[-i]
        k = k % money[-i]

print(ans)