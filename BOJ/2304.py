N = int(input())
changgo ={}
tt = 0
for _ in range(N):
    a, b = map(int, input().split())
    changgo[a] = b
    if tt < b:
        tt = b
        ttn = a

t = max(changgo.keys())

total = 0
num = 0
for i in range(1,ttn+1):
    if i in changgo.keys():
        if num < changgo[i]:       #창고가 더 크면 창고로 바꿔라
            num = changgo[i]
    total += num
num = 0
for i in range(t+1,ttn,-1):
    if i in changgo.keys():
        if num < changgo[i]:       #창고가 더 크면 창고로 바꿔라
            num = changgo[i]
    total += num
    
print(total)