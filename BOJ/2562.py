a = []
for i in range(9):
    a.append(int(input()))

mx = max(a)

max_num = a.index(max(a))+1

print(mx)
print(max_num)