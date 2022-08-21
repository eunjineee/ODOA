import sys
sys.stdin = open('swea1954.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    # 달팽이 칸 작성
    snail_list = [[-1]*N]
    for i in range(N-1):
        snail_list.append(snail_list[0][:])
    x = -1
    y = 0
    # 델타를 이용한 우선순위 작성 우 하 좌 상 순서
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 달팽이칸에 작성할 숫자
    cnt = 1
    # 달팽이 칸에 최대 숫자는 N*N이므로 while문을 통해서 반복
    while cnt <= N*N:
        # 우선순위를 이용하기 위한 반복문
        for i in range(4):
            while True:
                # 지금 바꿀 칸이 달팽이 인덱스 내에 존재하는가
                if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
                    # 지금 바꿀 칸이 아직 숫자를 쓰지 않은 칸인가
                    if snail_list[y+dy[i]][x+dx[i]] < 0:
                        snail_list[y+dy[i]][x+dx[i]] = cnt
                        x = x+dx[i]
                        y = y+dy[i]
                        cnt += 1
                    else:
                        break
                else:
                    break
		# 달팽이 칸을 위부터 순차적으로 문자열로 변환해서 출력
    print(f'#{Tc}')
    for i in range(N):
        result = ''
        for j in snail_list[i]:
            print(j, end=' ')
        print()