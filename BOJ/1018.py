m, n = map(int, input().split())
che = [list(input()) for _ in range(m)]
total =[]
for y in range(m-8+1):
    for x in range(n-8+1):
        cntw = 0
        cntb = 0
        for yy in range(y,y+8):
            for xx in range(x,x+8):
                if (yy + xx) % 2  == 0:
                    if che[yy][xx] != 'W':
                        cntw += 1 
                    if che[yy][xx] != 'B':
                        cntb += 1
                else:
                    if che[yy][xx] != 'B':
                        cntw += 1 
                    if che[yy][xx] != 'W':
                        cntb += 1
        total.append(cntw)
        total.append(cntb)
print(min(total))