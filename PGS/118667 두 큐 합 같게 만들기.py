from itertools import combinations 

def solution(queue1, queue2):
    total = queue1 + queue2
    totals = []
    for i in range(1,len(total)+1):
        totals += list(combinations(total, i))
    print(totals)
    answer = -2
    return answer

solution([3, 2, 7, 2], [4, 6, 5, 1])