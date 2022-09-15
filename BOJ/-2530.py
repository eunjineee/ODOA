a,b,c = map(int, input().split())
d = int(input())

e = (d//(60*60))
f = ((d%(60*60))//60)
k = ((d%(60*60))%60)

a = a + e
b = b + f
c = c + k

if c >= 60:
    c -= 60
    b+= 1
if b >= 60:
    b -= 60
    a += 1
if a >= 24:
    a -= 24
print(f'{a} {b} {c}')