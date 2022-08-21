import sys
sys.stdin = open('swea4836.txt')

T = int(input())
for t in range(1, T+1):
    ponum = int(input())    #ponum > point number
    total = [[0]*11 for _ in range(11)]
    cnt = 0
    for pn in range(ponum):
        a1, a2, b1, b2, co = map(int, input().split())
        for pointx in range(10):
            for pointy in range(10):
                if b1 >= pointx >= a1 and b2 >= pointy >= a2 and total[pointx][pointy] == 0:
                    total[pointx][pointy] = co
                elif b1 >= pointx >= a1 and b2 >= pointy >= a2 and total[pointx][pointy] != 0 and total[pointx][pointy] != co:
                    cnt += 1

    print(f'#{t} {cnt}')