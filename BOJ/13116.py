n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    aa= set()
    aa.add(a)
    while a > 0:
        a = a//2
        aa.add(a)
    bb = set()
    bb.add(b)
    while b > 0:
        b = b//2
        bb.add(b)
    
    print(max(aa & bb)*10)