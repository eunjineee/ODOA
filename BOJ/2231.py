b = int(input())
n =0
ans = 0
while n != b:
    to =sum(map(int,list(str(n))))
    if b == n + to:
        ans = n
        break
    n += 1


if ans > 0:
    print(ans)
else:
    print(0)