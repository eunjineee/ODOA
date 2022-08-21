N = int(input())

aa = []
for n in range(N):
    a = int(input())
    if a != 0:
        aa.append(a)
    else:
        aa.pop()
print(sum(aa))