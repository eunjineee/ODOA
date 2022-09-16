n = int(input())
a = 666
b = 0

if 5 >= n >= 1:
    ans = n*1000 + a
elif 12 >= n >= 6:
    ans = a*10 + (n-6)
else:
    num = (n-12) % 19
    mnum = (n-12) // 19 + 1
    if 9 >= num >= 1:
        ans = str(i+6) + str(a)
    else:
        ans = str(mnum)[-1] + str(istr(a)) + str(19-num)  

print(ans)