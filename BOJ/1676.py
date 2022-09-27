n = int(input())

ans = n
for i in range(n-1,0,-1):
    ans *= i

ans = str(ans)[::-1]

to = 0
for j in ans:
    if j != '0':
        break
    else:
        to += 1
if n==0:
    to = 0
print(to)