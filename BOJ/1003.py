<<<<<<< HEAD
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
=======

cnt_0 = 0
cnt_1 = 0

def fibo(n):
    global cnt_0
    global cnt_1
	if n == 0:
        cnt_0 += 1
		return 0
    elif n == 1:
        cnt_1 += 1
        return 1
	else:
		return fibo(n-1) + fibo(n-2)


>>>>>>> 32a137617703b9d48e25e7be9cab4c4fdd059e0a

t = int(input())
for i in range(t):
    c = int(input())
<<<<<<< HEAD
    cnt = (0, 0)
    cnt0 = (1,0)
    cnt1 = (0,1)
    fibo(c)
    print(*cnt)
=======
    fibo(c)
    print(cnt_0, cnt_1)
    
>>>>>>> 32a137617703b9d48e25e7be9cab4c4fdd059e0a
