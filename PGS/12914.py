# import math
# ans += math.factorial(one+two)//(math.factorial(one)*math.factorial(two))
# ↑ factorial 사용방법 

def f(a):
    num = 1
    for i in range(1, a+1):
        num *= i
    return num

def solution(n):
    one = n
    two = 0
    ans = 0
    while one >= 0:                          # 0까지도 아래에서 ans에 더해져야해서
        ans += f(one+two)//(f(one)*f(two))   # n! // (a!*(n-a)!)
        one -= 2
        two += 1
    
    return ans%1234567