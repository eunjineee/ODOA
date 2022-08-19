m, n = map(int, input().split())
che = [list(input().split()) for _ in range(n)]
for y in range(n-8+1):
    for x in range(m-8+1):
        for yy in range(8):
            for xx in range(7):
                if che[y+yy][x+xx] == 'W' and che[y+yy][x+xx+1] == 'B':
