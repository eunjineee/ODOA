from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)

    if (sum1+ sum2) // 2 == 1:        # 전체 합이 홀수이면 멈춰~
        answer = -1
        return answer

    q = q1 + q2
    if max(q) > (sum1 + sum2) // 2:   # 전체 합 //2 보다 제일 큰수 가 크면 멈춰
        answer = -1
        return answer
    
    num = 0
    while True:
        if sum1 > sum2:
            a = q1.popleft()
            q2.append(a)
            sum1 -= a
            sum2 += a
            num += 1
        elif sum1 < sum2:
            b = q2.popleft()
            q1.append(b)
            num += 1
            sum1 += b
            sum2 -= b
        else:
            answer = num
            break
        if num > len(queue1)*3:      # 최대 횟수 넘으면 멈춰~
            answer = -1
            break
    return answer


# print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
# print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
# print(solution([1, 1], [1, 5]))