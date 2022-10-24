from collections import deque
def score():   #점수 비교하기
    apeach_score = 0
    lion_score = 0
    for i in range(11):
        if apeach[i] >= lion[i]:
            apeach_score += (10-i)
        else:
            lion_score += (10-i)
        
def ans_find():
    ans.sort(reverse=True)
    answer = ans[0]

def 채우기():
    lion = [0]*(n+1)
    q = [0,1,2,3,4,5,6,7,8,9,10]
    p = [-1, 0 , 0]
    while q:
        t = q.popleft()
        for j in range(3):
            num = lion[t]
            if to < n and j != 2:
                num = num + p[j]
                if 0 < num <=n and total+num <= n:
                    lion[t] = num
                    total += num
            elif to < n and j == 2:
                num = 0






def solution(n, info):
    ans = []

        



    answer = []
    return answer



# solution(5, [2,1,1,1,0,0,0,0,0,0,0])