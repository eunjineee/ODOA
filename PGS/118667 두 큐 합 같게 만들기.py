from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1.reverse()
    q2.reverse()
    if sum(q1) == sum(q2):
        num = 1
    else:
        num = 0
        ans = []
        while q1:
            a = q1.popleft()
            q2.append(a)
            num += 1
            if sum(q1) == sum(q2):
                ans.append(num)

        q1 = deque(queue1)
        q2 = deque(queue2)
        q1.reverse()
        q2.reverse()
        num = 0
        while q2:
            a = q2.popleft()
            q1.append(a)
            num += 1
            if sum(q2) == sum(q1):
                ans.append(num)
        print(ans)
                
    
    answer = -2
    return answer

solution([3, 2, 7, 2], [4, 6, 5, 1])