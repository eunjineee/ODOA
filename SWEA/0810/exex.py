import sys
sys.stdin = open('swea1954.txt')
T = int(input())
for t in range(1,T+1):
    num = int(input())
    matrix = [[0]*num for _ in range(num)] # 행렬 제작
    direction_x = [1,0,-1,0] # 우하좌상으로 이동
    direction_y = [0,1,0,-1]
    matrix[0][0] = 1
    #start point
    x = num-1
    y = 0
    count = 1

    for i in range(num):
            matrix[0][i] = count
            count += 1   # 4
    time = 1
    while count <= num * num: # nnn, n-1, n-1
        for j in range(num-1,0,-1): # 2번식
            for p in range(2):
                for k in range(j):
                    matrix[y+direction_y[time]][x+direction_x[time]] = count
                    x = x+direction_x[time]
                    y = y+direction_y[time]
                    count += 1
                time += 1
                time %= 4
    print(f'#{t}')
    for a in range(num):
        for b in range(num):
            print(matrix[a][b],end=" ")
        print("\n")