n = list(input())

total = []
a = ''
for i in n:
    if i == '+':
        total.append(a)
        a = ''
        total.append(i)
    elif i == '-':
        total.append(a)
        a = ''
        total.append(i)
    else:
        a += i
print(total)

for j in len(total):
    if total[j] == '+':
        total[j-1] + total[j+1]