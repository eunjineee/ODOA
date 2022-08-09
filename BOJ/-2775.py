n = int(input())

for i in range(n):
    k = int(input())
    n = int(input())
    li = []
    li2 = []

    for j in range(1, n+1):
        li.append(j)
        li2.append(0)
    for s in range(1,k):
        for x in range(1,n+1):
            li2[x] = sum(li[::x])
        li = li2[:]
    print(li)

