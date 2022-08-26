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
n = 0
m = 0
jeonx = []
jeony = []
for _ in range(3):
    jeonx.append(abs(jeonche[n+1][0]-jeonche[n][0]))
    n += 2
    jeony.append(abs(jeonche[m+1][1]-jeonche[m][1]))
    m += 2

jeonx.sort()
jeony.sort()


total = abs(jeonx[2]) * abs(jeony[2]) - abs(jeonx[2]-jeonx[0]) * abs(jeony[2]-jeony[1])
print(total*n)