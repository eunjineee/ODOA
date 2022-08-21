import sys
sys.stdin = open('swea4839.txt')

T = int(input())

for t in range(1, T+1):
    p, a, b = map(int, input().split())
    point = [a,b]
    c = 0
    for i in range(len(point)):
        num = 0
        start = 1
        end = p
        while c != point[i]:
            c = (start + end) // 2
            if point[i] > c :
                start = c
            else:
                end = c
            num += 1
        point[i] = num
    if point[0] > point[1]:
        print(f'#{t} B')
    elif point[0] < point[1]:
        print(f'#{t} A')
    else:
        print(f'#{t} 0')