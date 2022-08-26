def nam(listt, su):
    for i in range(len(listt)):
        if (i+1) % su == 0:
            if listt[i] == 0:
                listt[i] = 1
            else:
                listt[i] = 0
    return listt

def yeo(listt, su):
    n = len(listt)
    if n > su > 1:
        a = False
        i = 1
        while a != True:
            if n-1 >= su-1+i >= 0 and n-1 >= su-1-i >= 0:
                if listt[su-1+i] == listt[su-1-i]:
                    i += 1
                else:
                    a = True
            else:
                a = True
        i -= 1
        for e in range(su-1-i,su-1+i+1):
            if listt[e] == 0:
                listt[e] = 1
            else:
                listt[e] = 0
    else:
        if listt[su-1] == 0:
            listt[su-1] = 1
        else:
            listt[su-1] = 0
    return listt



n = int(input())
click = list(map(int, input().split()))
saram = int(input())
for ingan in range(saram):
    sungbeal, sutza = map(int, input().split())
    if sungbeal == 1:
        click = nam(click, sutza)
    else:
        click = yeo(click, sutza)

for q in range(1,len(click)+1):
    if q % 20 == 0:
        print(click[q-1])
    else:
        print(click[q-1],end=' ')    