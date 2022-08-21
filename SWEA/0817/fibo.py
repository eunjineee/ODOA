# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# for i in range(101):
#     print(i, fibo(i))    #중복호출 횟수가 많아져서 31부터는 느려짐

#2 메모리제이션 시간이 많이 줄어들고 바로 나옴
def fibo(n):
    if memo[n]==-1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1] * 101
memo[0] = 0
memo[1] = 1
for i in range(101):
    print(i, fibo(i))