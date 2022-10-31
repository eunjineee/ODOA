from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    # q1.reverse()
    # q2.everse()
    if (sum(q1) + sum(q2)) // 2 == 1:
        answer = -1
        return answer

    if sum(q1) == sum(q2):
        answer = 1
        return answer
    else:
        num = 0
        ans = []
        while q1:
            a = q1.popleft()
            q2.append(a)
            num += 1
            if sum(q1) == sum(q2):
                ans.append(num)
            b = q2.popleft()
            q1.append(b)
            num += 1
            if sum(q1) == sum(q2):
                ans.append(num)
            if num > len(queue1)*2 + 1:
                break

        # q1 = deque(queue1)
        # q2 = deque(queue2)
        # # q1.reverse()
        # # q2.reverse()
        # num = 0
        # while q2:
        #     a = q2.popleft()
        #     q1.append(a)
        #     num += 1
        #     if sum(q2) == sum(q1):
        #         ans.append(num)
        print(ans)
                
    
        answer = min(ans)
        return answer

solution([3, 2, 7, 2], [4, 6, 5, 1])
solution([1, 2, 1, 2], [1, 10, 1, 2])
solution([1, 1], [1, 5])