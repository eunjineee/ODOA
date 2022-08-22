def f(i, N):
    if i == N:
        print(bit)
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * 10
f(0, 10)