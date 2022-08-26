def daum(start,jusawui,i):
    indexxx = jusawui[i].index(start)
    daumsu = jusawui[i][jogun[indexxx]]
    if (start == 6 and daumsu == 5) or (start == 5 and daumsu == 6):
        namunsu = 4
    elif start == 6 or daumsu == 6:
        namunsu = 5
    else:
        namunsu = 6
    return (daumsu, namunsu, i)
    

n = int(input())
tong = [list(map(int, input().split())) for _ in range(n)]
jogun = [5,3,4,1,2,0]
namunsu = 0
ans = []
for j in range(1,7):
    cheoum = j
    sunseo = 0
    total = 0
    for z in range(n):
        cheoumcheorum, susu, sunseo = daum(cheoum,tong,sunseo)
        sunseo += 1
        total += susu
        cheoum = cheoumcheorum
    ans.append(total)
print(max(ans))