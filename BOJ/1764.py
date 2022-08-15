import sys
a, b = map(int,input().split())

ddbodo = {}
for _ in range(a+b):
    dd = (sys.stdin.readline().rstrip())
    if dd in ddbodo:
        ddbodo[dd] = 2
    else:
        ddbodo[dd] =1
total = []

for n, num in ddbodo.items():  
    if num == 2:
        total.append(n)

print(len(total))
for i in sorted(total):
    print(i)