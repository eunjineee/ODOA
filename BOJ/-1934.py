a = int(input())

b ,c = map(int, input().split())
bb = []
cc = []
tt = 1
for i in range(a):
    for bsmall in range(1,b+1):
        if b % bsmall == 0:
            bb.append(bsmall)
    for csmall in range(1,c+1):
        if c % csmall == 0:
            cc.append(csmall)

    for z in bb:
        total = cc[:] 
        bz=bb.count(z)
        cz=cc.count(z)
        if bz >= cz:
            total.append(z**bz)
        else:
            total.append(z **cz)
    for y in total:
        tt *= y
    print(tt)