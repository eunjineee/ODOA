n = int(input())
x = 0
y = 0
jeonche =[]

for _ in range(6):
    banghang , size = map(int, input().split())
    if banghang == 1:
        jeonche.append([x+size,y])
        x += size
    elif banghang == 2:
        jeonche.append([x-size,y])
        x-= size
    elif banghang == 3:
        jeonche.append([x,y-size])
        y-=size
    elif banghang == 4:
        jeonche.append([x,y+size])
        y+=size
jeonche.sort()
jeonx = []
jeony = []
for p in range(6):
    jeonx.append(jeonche[p][0])
    jeony.append(jeonche[p][1])

jeonx.sort()
jeony.sort()
to = [0, -1]

for i in to:
    for j in to:
        if [jeonx[to[i]],jeony[to[j]]] not in jeonche:
            merong = (jeonx[to[i]],jeony[to[j]])
            break

total = abs(jeonx[-1]-jeonx[0]) * abs(jeony[-1]-jeony[0]) - abs(jeonx[2]-merong[0]) * abs(jeony[2]-merong[1])
print(total*n)