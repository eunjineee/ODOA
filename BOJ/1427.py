n = input()
m = []
for i in range(len(n)):
    m.append(n[i])
m.sort(reverse=True)

for j in m:
    print(j,end="")