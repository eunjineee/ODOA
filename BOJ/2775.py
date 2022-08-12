n = int(input())

for i in range(n):
    k = int(input())
    n = int(input())
    li = []
    li2 = []
    for j in range(1, n+1):          #0층을 만들어줌
        li.append(j)
    for s in range(k):               #층수가 올라감
        for x in range(1,n+1):       #호수가 올라감
            li2.append(sum(li[:x]))  #층수 올라갈때마다 리스트 변경
        li = li2[:]
        li2=[]
    print(li[-1])

