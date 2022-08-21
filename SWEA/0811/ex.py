#홍민님의 사다리타기
import sys
sys.stdin = open('1210.txt')

T = 10
for _ in range(T):
    N = int(input()) # 테스트 케이스 번호

    # 2차원 배열로 100*100 을 arr에 담기
    arr = [list(map(int,input().split())) for _ in range(100)]

    #    위, 오른쪽,왼쪽
    di = [-1, 0, 0]
    dj = [0, 1, -1]

    f_i, f_j = 0, 0  # 해당 위치의 값이 2인 좌표를 체크하기 위한 변수
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:  # 도착지점인 2의 좌표 찾기
                f_i , f_j = i, j

    while True:
        if f_j+1 <= 99 and arr[f_i][f_j+1] == 1: # 오른쪽에 길이 있다면
            arr[f_i][f_j] = 0 # 기존의 좌표 값은 0으로 변경
            f_i , f_j = f_i+di[1], f_j+dj[1] # 좌표값 변경 (오른쪽으로 한칸 이동)

        elif f_j - 1 >= 0 and arr[f_i][f_j - 1] == 1 :  # 왼쪽에 길이 있다면
            arr[f_i][f_j] = 0  # 기존의 좌표 값은 0으로 변경
            f_i, f_j = f_i + di[2], f_j + dj[2]

        elif f_i - 1 >= 0  and arr[f_i-1][f_j] == 1:  # 위에 길이 있다면
            arr[f_i][f_j] = 0  # 기존의 좌표 값은 0으로 변경
            f_i, f_j = f_i + di[0], f_j + dj[0]

        # 이동한 f_i 라고 하는 i의 값이 0의 경우 가장 위쪽이기에 while문 탈출
        if f_i == 0:
            break

    print(f'#{N} {f_j}')