N = int(input())
c= [0] * 12
for z in range(N):
   arr = list(map(int, input().split()))
    tmp = [0] * N
    c = [0] * 101
    for i in range(N):
        c[arr[i]] += 1
    for j in range(1, 101):
        c[j] += c[j - 1]
    for i in range(N - 1, -1, -1):
        c[arr[i]] -= 1
        tmp[c[arr[i]]] = arr[i]
    print(tmp)

    x = 0
    tri = run = 0
    while x < 10 :
        if tmp[x] >= 3:
            tmp[x] -= 3
            tri += 1
            continue
        if tmp[x] >= 1 and tmp[x+1] >= 1 and tmp[x+2] >= 1 :
            tmp[x] -= 1
            tmp[x+1] -= 1
            tmp[x+2] -= 1
            run += 1
            continue
        x += 1
    if run + tri == 2:
        print("Baby Gin")
    else:
        print("Lose")