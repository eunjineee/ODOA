def f(i, N, s, t):
    global  answer
    if i == N:                  #모든 원소가 고려된 경우
        if s == t:              #부분집합의 합이 t면
            answer += 1
        return
    else:
        f(i+1, N, s+A[i], t)    #A[i]가 포함된 경우
        f(i+1, N, s, t)         #A[i]가 포함되지 않은 경우

N, s = map(int, input().split())
A = list(map(int,input().split()))
bit = [0] * N
answer = 0
if s == 0 :
    answer -= 1
f(0, N, 0, s)
print(answer)