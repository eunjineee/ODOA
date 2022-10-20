t = int(input())

def nCr(a, b, s):
    global ans
    if b == 0:
        ans += 1
    else:
        for i in range(s, a-b+1):
            comb[b-1] = A[i]
            nCr(a, b-1, i+1)
            


for _ in range(t):
    n, m = map(int,input().split())
    a = max(n,m)
    b = min(n,m)
    ans = 0
    A = [j for j in range(a)]
    comb = [0] * b

    nCr(a, b, 0)
    print(ans)