from math import sqrt
def solution(brown, yellow):
    total_answer = []
    answer = []
    for i in range(1,int(sqrt(yellow))+1):
        if yellow % i == 0:
            answer.append((i,yellow//i))
    for (a,b) in answer:
        if (a+b)*2 + 4 == brown:
            total_answer.append(b+2)
            total_answer.append(a+2)
    # return sorted(total_answer,reverse=True)
    return total_answer

print(solution(10,2)) 
print(solution(8,1)) 
print(solution(24,24)) 