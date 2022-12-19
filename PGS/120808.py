def solution(denum1, num1, denum2, num2):
    answer = []
    answer.append(denum1*num2 + denum2*num1)
    answer.append(num1*num2)
    for i in range(max(answer),0,-1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            answer[0] = answer[0] // i
            answer[1] = answer[1] // i
    return answer

print(solution(1,2,3,4))