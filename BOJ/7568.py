a=int(input())
li=[]
for i in range(a):
    li.append(list(map(int, input().split())))
for j in li:
    lank = 1
    for z in li:
        if j[0] < z[0] and j[1] < z[1]:
            lank += 1
    print(lank, end=" ")