N,M = map(int, input().split())
arr = list(range(1,N+1))
chosen = [0]*M

def comb(n,m,j):
    if n == m:
        print(*chosen)
        return
    else:
        for i in range(j,N):
            chosen[n] = arr[i]
            comb(n+1,m,i+1)
comb(0,M,0)

def perm(n,m):
    if n == m:
        print(*chosen)
        return
    else:
        for i in range(N):
            if i in chosen:
                continue
            chosen[n] = arr[i]
            comb(n+1,m)
            chosen[n] = 0
comb(0,M)