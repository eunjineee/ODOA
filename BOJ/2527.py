for _ in range(4):
    a,b,c,d,e,f,g,h=map(int, input().split())
    aa = [(a,b),(a,d),(c,b),(c,d)]
    bb = [(e,f),(e,h),(g,f),(g,h)]

    if e > c or d < f or g < a or b > h:
        print('d')
    elif (
        (a == g and f == d) or
        (c == e and d == f) or
        (c == e and b == h) or
        (g == a and h == b)):
        print('c')
    elif c == e or b == h or a == g or d == f:
        print('b')    
    else:
        print('a')