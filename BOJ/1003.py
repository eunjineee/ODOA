
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



t = int(input())
for i in range(t):
    c = int(input())
    fibo(c)
    print(cnt_0, cnt_1)
    