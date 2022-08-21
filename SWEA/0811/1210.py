import sys
sys.stdin = open('1210.txt')
for t in range(10):
    T = int(input())
    ground = [list(map(int,input().split()))+[0]+[0] for _ in range(100)]
    #당첨(2) 찾기
    x0 = 0
    for i in ground[99]:
        x0 += 1
        if i == 2:
            break
    #위로 올라가다가 왼오중에 1있으면 (범위 안에도 있어야함) 고고링
    x,y = [x0, 99]
    while y != 0:
        if ground[y][x-1] == 1 and 100 >= x >= 0:
            x = x - 1
            ground[y][x] = 0

        elif ground[y][x+1] == 1 and 100 >= x >= 0:
            x = x + 1
            ground[y][x] = 0
        else:
            y = y - 1
            ground[y][x] = 0
    print(f'#{T} {x}')
