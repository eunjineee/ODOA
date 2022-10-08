n = int(input())
m = int(input())
mun = input()

i = 0
num = 0
ans = 0
while i <= m:
    if mun[i:i+3] == "IOI":
        num += 1
        i += 2
        if num == n:
            ans += 1
            num -= 1
    else:
        num = 0
        i += 1
print(ans)