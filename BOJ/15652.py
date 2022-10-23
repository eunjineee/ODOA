import time
start = time.time()
def nPr(r,li):
    if r == M:
        # print(*li[1:])
        return
    for a in arr:
        if a >= li[-1]:
            nPr(r+1, li+[a])
N, M = map(int, input().split())
arr = list(range(1, N+1))
nPr(0,[0])  # r
print("time :", time.time() - start)