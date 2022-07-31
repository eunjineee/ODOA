a = input().upper()
aa = list(set(a))
b ={}
for i in aa:
    b[i] = a.count(i) 
    
cnt = []
for key, value in b.items():
    if value == max(b.values()):
        cnt.append(key)
if len(cnt)!= 1:
    print('?')
else:
    print(cnt[0])