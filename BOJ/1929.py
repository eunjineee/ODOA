n, m = map(int, input().split())

if n < 2:
    n = 2
a = 2

for i in range(n,m+1):
    for j in range(a,int(i**0.5)+1):      #제곱근까지만 판별하기⭐
        if i % j == 0:
            break
    else:
        print(i)
        a == i