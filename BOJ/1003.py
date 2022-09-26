import sys
input = sys.stdin.readline
def fibo(n):
    global cnt0
    global cnt1
    global cnt
    if n == 0:
        cnt = cnt0
    elif n == 1:
        cnt = cnt1
    else:
        for j in range(1,n):
            cnt = (cnt0[0] + cnt1[0], cnt0[1] + cnt1[1])
            cnt0 = cnt1
            cnt1 = cnt

t = int(input())
for i in range(t):
    c = int(input())
    cnt = (0, 0)
    cnt0 = (1,0)
    cnt1 = (0,1)
    fibo(c)
    print(*cnt)
