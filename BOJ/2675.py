T = int(input())
for t in range(T):
    a, b = input().split()
    p =''
    for bb in b:
        p += bb*int(a)
    print(p)