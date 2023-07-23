# def solution(queries):
#     answer = []
#     ans_dict = {'1':['RR']*4, '2':['RR','Rr','Rr','rr'], '3':['rr']*4}
#     for k,l in queries:
#         n = 4**k
#         if n//4 > l and l > n-(n//4):
            
#         total.append(answer[k-1][l-1])
#     return total

# # print(solution([[3, 8]]))
# print(solution([[3, 5]]))
# print(solution([[3, 8], [2, 2]]))
# print(solution([[3, 1], [2, 3], [3, 9]]))
# print(solution([[4, 26]]))


def get_gene(pose):
    n, p = pose
    stack = []
    
    p -= 1
    while n>1:
        stack.append(p%4)
        n -= 1
        p //= 4
    
    while len(stack) > 0:
        num = stack.pop()
        if num == 0: return 'RR'
        if num == 3: return 'rr'
    return 'Rr'

def solution(queries):
    return [*map(get_gene, queries)]

# print(solution([[3, 5]]))
# print(solution([[3, 8], [2, 2]]))
# print(solution([[3, 1], [2, 3], [3, 9]]))
print(solution([[4, 26]]))