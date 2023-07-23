def solution(emergency):
    answer = []
    e = emergency[::]
    e.sort()
    for i in emergency:
        answer.append(e.index(i)+1)
    return answer
print(solution([3, 76, 24]))