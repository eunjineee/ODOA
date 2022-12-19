a,b,c= map(int, input().split())
if b == 1:
    print(a%c)
else:
    e = power(a,b//2)
    if b%2 == 0:
        print(e*e%c)
    else:
        print(e*e*a%c)
