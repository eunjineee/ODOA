from itertools import combinations_with_replacement

def solution(n, info):
    lion_nums = list(combinations_with_replacement(range(0,11),n))    #냅다 함수쓰기
    print(lion_nums)
    maxcha = float("-inf")
    answer = [-1]
    for lion_num in lion_nums:
        lion = [0] * 11
        for score in lion_num:           #lion에 어피치 점수(info)와 같은 모양으로 넣어주기
            lion[10 - score] += 1
        
        apeach_score = 0
        lion_score = 0
        for i in range(11):
            if info[i] == lion[i] == 0:    #0일때는 지나가기
                continue
            elif info[i] >= lion[i]:  
                apeach_score += (10-i)
            else:
                lion_score += (10-i)

        if lion_score > apeach_score:          #점수 비교할때, lion_nums가 0이 많은 순서로 만들기 때문에
            chai = lion_score - apeach_score
            if chai > maxcha:                  #차이가 가장 큰것을 먼저 answer에 넣어주면 끝까지 가져감
                maxcha = chai
                answer = lion
    return answer

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))

# lion_nums = [
#     (0, 0, 0, 0, 0), 
#     (0, 0, 0, 0, 1), 
#     (0, 0, 0, 0, 2), 
#     (0, 0, 0, 0, 3), 
#     (0, 0, 0, 0, 4), 
#     (0, 0, 0, 0, 5), 
#     (0, 0, 0, 0, 6), 
#     (0, 0, 0, 0, 7), 
#     (0, 0, 0, 0, 8), 
#     (0, 0, 0, 0, 9),
#     ...
#     ]