n=int(input())

if n == 1:
    print(1)
else:
    b = 1
    n -= 1
    while n > 0:
        n -= 6*b
        b += 1
    print(b)