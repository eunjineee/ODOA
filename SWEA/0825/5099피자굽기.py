import sys
sys.stdin = open('swea5099.txt')

from collections import deque


def pizzamaker(cheese,hwaducksize,pizzas):               #피자 치즈 양, 화덕 크기, 만들피자 개수
    maker = deque(cheese[j] for j in range(hwaducksize)) #화덕 크기만큼 피자 넣기

    while len(maker) != 1:                               #피자 메이커에 1개 남을때까지 구워
        maker[0][1] = maker[0][1] // 2                   #첫번째꺼 구워서 치즈 반띵 + 19번줄로 가서 뒤로 빼기
        if maker[0][1] == 0:                             #치즈 0됐으면
            maker.popleft()                              #피자 완성(화덕에서 뺌)
            if hwaducksize >= pizzas:                    #화덕사이즈는 화덕에 가져오는 피자 갯수
                continue                                 #빼고나면 넣어줄건데 만들어야하는 수 m보다 많아지면 화덕에 그만 넣어
            else:
                maker.append(cheese[hwaducksize])        #다음 만들어야하는거 화덕에 넣기
                hwaducksize += 1                         #다음피자 정해줌
        maker.rotate(-1)
    print(f'#{t+1} {maker[0][0]+1}')                     #몇번째 피자니? (0부터 시작해서 +1)

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    cheeeeeeese = {}
    for i in range(m):
        cheeeeeeese[i] = [i, a[i]]                       #딕셔너리 안에 리스트 형태로 가져옴 (0번째피자:[0번,치즈양x])
    pizzamaker(cheeeeeeese,n,m)