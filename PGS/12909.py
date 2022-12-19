def solution(s):
    answer = []
    if s[0] == ')' or s[-1] == '(':
        return False
    for i in s:
        if i == '(':
            answer.append(1)
        else:
            if len(answer) != 0:
                answer.pop()
            else:
                return False
    if len(answer) != 0:
        return False
    return True

print(solution(")()("))