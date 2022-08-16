a, b = map(int, input().split())
aa=1
bb=1

for i in range(1,b+1):
    aa *= a+1-i
    bb *= i

print(aa//bb)
