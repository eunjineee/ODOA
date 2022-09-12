def f(i, N):
    global  ans
    if i == N:
        s= 0                    
        for i in range(N):
            if bit[i]:
                s += 1
        if s == m:
            ans += 1        
            for i in range(N):
                if bit[i]:
                    print(A[i], end = ' ')
            print()
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

n, m =map(int, input().split())
A = list(range(1,n+1))
bit = [0] * n
ans = 0
f(0, n)