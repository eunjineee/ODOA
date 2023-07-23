from itertools import permutations
def solution(ability):
    answer = 0
    
    p = list(permutations(ability, len(ability[0])))
    print(p)
    for i in range(len(p)):
        total = 0
        for j in range(len(p[i])):
            total += p[i][j][j]
        answer = max(answer, total)
    return answer

# print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
# print(solution([[20, 30], [30, 20], [20, 30]]))
print(solution([[1, 2], [3, 4], [5, 6]]))