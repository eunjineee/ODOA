def solution(n):
    answer = 0
    
    number = 0
    turn = 1
    while number < n:
        number += turn
        turn += 1

    re = 0
    for i in range(1, turn):
        re += (i-1)
        if (n-re) % i == 0:
            answer += 1
    return answer

print(solution(15))