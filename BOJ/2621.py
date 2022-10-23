dic = {}

for i in ['R', 'B', 'Y', 'G']:
    dic[i] = [0,[]]
li = [0]*10
numli = []

for _ in range(5):
    a, b = input().split(' ')
    b = int(b)
    dic[a][0] += 1
    dic[a][1].append(b)
    numli.append(b)
    li[b] += 1

maxnum = 0
minnum = 0
for j in dic.values():
    if j[0] > maxnum:
        maxnum = j[0]
    if i[0] != 0 and j[0] < minnum:
        minnum = j[0]

ans = []
#1
if max(li) == 5:
    ans.append(max[li] + 900)
#2
if max(li) == 4:
    ans.append(max[li] + 800)
#3
if max(li) == 3 and min(li) == 2:
    ans.append(li.index(max[li])*10 + li.index(min[li]) +700)
#4
if maxnum == 5:
    ans.append(max[numli] + 600)
#5
numli.sort()
for jj in range(4):
    if numli[jj] != numli[jj+1]:
        break
    ans.append(numli[-1] + 500)
#6
if 3 in li:
    ans.append(400 + numli.index(3))
#7
t = 0
tt = []
for k in range(len(li)):
    if li[k] == 2:
        t += 1
        tt.append(k)
if t == 2:
    ans.append(300+tt[1]*10+tt[0])
#8
if len(tt) == 1:
    ans.append(tt[0]+200)
#9
if len(ans) == 0:
    ans.append(numli[-1] +100)

print(max(ans))