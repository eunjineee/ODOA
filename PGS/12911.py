def solution(n):
    num = str(bin(n)[2:]).count('1')
    print(num)
    while True:
        n += 1
        n_number = str(bin(n)[2:]).count('1')
        if num == n_number:
            break
    return n
print(solution(15))

