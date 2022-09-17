a, b = map(int,list(input()))
aa = a*10 + b
num = 0

while c != aa:
    c = str(a + b)
    to = a
    to += b[-1]
    num += 1

print(num)
    
    