from itertools import combinations
def solution(orders, course):
    total = []
    for cou in range(len(course)):
        ans = {}
        answer = []
        for i in orders:
            a = list(combinations(i,course[cou]))
            answer += a
        for j in answer:
            if j in ans:
                ans[j] += 1
            else:
                ans[j] = 1
        ansmax = max(list(ans.values()))
        for k in ans:
            if ans[k] == ansmax:
                toto = ''
                for kk in range(len(k)):
                    toto += k[kk]
                total.append(toto)
    return total