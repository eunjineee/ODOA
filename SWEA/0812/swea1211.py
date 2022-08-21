findnum = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

a= int(input())
for aa in range(a):
    t, ns = input().split()
    sou = input()
    ns = int(ns)
    totalnum = []
    for i in findnum:
        for idx in range(len(sou)-len(i) + 1):
            for j in range(len(i)):
                if sou[idx + j] != i[j]:
                    break
            else:
                totalnum.append(i)
    print(t)
    for to in totalnum:
        print(to,end=' ')