def solution(n,a,b):
    answer = 0
    li = [i for i in range(1,n+1)]
    while len(li) != 1:
        li2 = []
        for j in range(len(li)//2):
            x, y = li[j*2], li[j*2+1]
            if x == a or x == b:
                if y == a or y == b:
                    return answer + 1
                li2.append(x)
            else:
                li2.append(y)
        answer += 1
        li = li2


print(solution(8,4,7))