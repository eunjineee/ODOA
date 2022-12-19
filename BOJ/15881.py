m = int(input())
n = input()
ans = 0
a = 0
while a < m:
    if n[a:a+4] == 'pPAp':
        a += 4
        ans += 1
    else:
        a += 1 
print(ans)