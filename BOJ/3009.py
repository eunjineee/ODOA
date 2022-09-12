aa = []
bb = []
for _ in range(3):
    a, b = map(int, input().split())
    aa.append(a)
    bb.append(b)
for i in aa:
    if aa.count(i) == 1:
        totala = i
for j in bb:
    if bb.count(j) == 1:
        totalb = j 
print(str(totala) +' '+ str(totalb))       