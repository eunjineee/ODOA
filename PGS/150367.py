def solution(numbers):
    answer = []
    for i in numbers:
        a = bin(int(i))
        b = a[2::]
        print("turn",i ,b)
        print("turn", len(b))
        #짝수면 처음에 0 추가
        if len(b)%2 == 0:
            b1 = '0'+ b
            answer.append(check(b1))
        else:
            answer.append(check(b))
    return answer

def check(number):
    for j in range(1,len(number)+1):
        if j%2 == 0:  #짝수면(1,2,3...)
            if number[j-1] == '0':
                return 0  #무조건 안됌
        else: #홀수는 상관없음
            pass
    return 1


# print(solution([5,95]))
print(solution([7, 42, 5, 63, 111, 95]))
# print(solution([10000]))