
a = int(input())
b = int(input())

total = []
smallnum = 100001
for i in range(a, b+1):
    if i > 2:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            total.append(i)
    elif i == 2:
        total.append(2)


if len(total) > 0:
    print(sum(total))
    print(total[0])
else:
    print(-1)