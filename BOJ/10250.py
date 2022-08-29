T = int(input())
for t in range(T):
    h, w, n = map(int,input().split())
    hosu = n//h +1
    floor = n % h
    if n % h == 0:
        hosu = n//h
        floor = h
    print(f'{floor*100 + hosu}')