for _ in range(4):
    a,b,c,d,e,f,g,h=map(int, input().split())
    aa = [(a,b),(a,d),(c,b),(c,d)]
    bb = [(e,f),(e,h),(g,f),(g,h)]

    for q in aa:
            for w in bb:
                if q == w:
                    print('c')
                    continue
    xx = [a,c,e,g]
    yy = [b,d,f,h]
    cnt = 0
    for x in xx:
        for y in yy:
            if x == y:
                cnt += 1
    if cnt == 1:
        print('b')
        continue    
    elif b < f < d or b < h < d or a < e < c or a < g < c:
        print('a')
        
    else:
        print('d')