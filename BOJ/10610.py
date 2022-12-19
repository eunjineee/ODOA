num = []
for i in range(8):
    num.append((int(input()),i+1))

num.sort()
num = num[-5:]

ans1 = 0
ans2 = []

for j in num:
    ans1 += j[0]
    ans2.append(j[1])
ans2.sort()
print(ans1)
print(*ans2)