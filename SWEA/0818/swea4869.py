T = int(input())

for t in range(T):
    N = int(input())
    y = N//10
    num = [0, 1, 3]
    a = 2
    if y >= 2:
        while a != y:
            if a % 2 == 0 :
                num.append(num[a]*2-1)
            else:
                num.append(num[a]*2+1)
            a += 1
    print(f'#{t+1} {num[y]}')