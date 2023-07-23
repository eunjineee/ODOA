def solution(n):
    answer = []
    num = 0 
    for i in range(1,n+1):                          # 사각형 만들면서 반은 -1로 채워서 삼각형으로 만듦
        answer.append([0]*i+[-1]*(n-i))
        num += i                                    # 끝나는 숫자도 확인 
    # print(num)
    # print(answer)
    a,b = 0,0
    dd = [(1,0),(0,1),(-1,-1)]
    d = 0                                           # dd의 순서
    answer[0][0] = 1                                # (0, 0)에 1 포함시키고 시작
    for i in range(2, num+1):
        if 0<=a+dd[d][0]<n and 0<=b+dd[d][1]<n:     # 사각형을 돌 때, 범위를 벗어나면 d를 바꿔줌
            a,b = a+dd[d][0], b+dd[d][1]
            if answer[a][b] == 0:
                answer[a][b] = i
                # print(answer)
            else:                                   # 0이 아니면, d를 바꿔줌
                if d == 2:
                    d = 0
                    # a,b = a+2, b+1
                    a,b = a-dd[d-1][0]+dd[d][0], b-dd[d-1][1]+dd[d][1]  # 삼각형으로 돌고 있던 경우, d-1인 경우를 빼고 다시 돌려줌
                    answer[a][b] = i
                    # print(answer)
                else:
                    d += 1
                    a,b = a-dd[d-1][0]+dd[d][0], b-dd[d-1][1]+dd[d][1]
                    answer[a][b] = i
                    # print(answer)
        else:
            if d == 2:
                d = 0
            else:
                d += 1
                a,b = a+dd[d][0], b+dd[d][1]
                answer[a][b] = i
                # print(answer)
        
    totalans = []
    for ans in answer:
        for s in ans:
            if s != -1:
                totalans.append(s)

    return totalans

print(solution(4))
print(solution(5))