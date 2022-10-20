n = int(input())
dp = [0] * (n+1)
m = n
ans = 0
while n != 0:
    if (n ** (1/2)) % 1 > 0:
        n -= 1
    else:
        m -= n
        ans += 1
        n = m

print(ans)