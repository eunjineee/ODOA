n = int(input())

queen = [0]*n


def f(a):
    global ans
    queen[a] = 1
    if a == n:
        ans += 1
    else:
        for j in range(n):
            if queen[j] == 0:
                f(j)

ans = 0
for i in range(n):
    f(i)
print(ans)
