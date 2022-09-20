l = int(input())
st = input()
total = 0

for i in range(l):
    total += (ord(st[i])-96) * 31**(i)

print(total%1234567891)