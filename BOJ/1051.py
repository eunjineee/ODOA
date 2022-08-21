n, m = map(int, input().split())
nums = [list(input()) for _ in range(n)]

if m < n :
    a = m
else:
    a = n
to = []

for i in range(n):
    for j in range(m):
        try:
            for k in range(a):
                if nums[i][j] == nums[i][j+k] == nums[i+k][j] == nums[i+k][j+k]:
                    to.append(k)
        except IndexError:
            continue

ans = (max(to)+1)**2

print(ans)