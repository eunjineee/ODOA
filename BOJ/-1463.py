n = int(input())
ans = 0
while n != 1:
    if n % 3 == 0:
        n = n//3
    elif n % 2 == 0: 
        n = n//2
    else:
        n -= 1
    ans += 1

print(ans)