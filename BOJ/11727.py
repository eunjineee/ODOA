n = int(input())
num = [0, 1, 3]
a = 2
if n >= 2:
    while a != n:
        if a % 2 == 0:
            num.append(2*num[a]-1)
        else:
            num.append(2*num[a]+1)
        a += 1
        
print(num[n]%10007)