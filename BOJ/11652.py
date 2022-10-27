n = int(input())
dic = {}

for _ in range(n):
    i = int(input())
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

ans = max(dic.values())

answer = (2**62)+1
for j, k in dic.items():
    if k == ans and j < answer:
        answer = j
print( answer )

