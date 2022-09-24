import sys
input = sys.stdin.readline
n, m, bag = map(int, input().split())
ground = []

for _ in range(n):
    ground += list(map(int, input().split()))

gmax = max(ground)

total = sys.maxsize
totalnum = 0
for i in range(gmax+1):
    ans1 = ans2 = 0
    time = 0
    for j in ground:
        if j > i :
            ans1 += (j-i)
            time += (j-i) * 2
        elif j < i:
            ans2 += (i-j)
            time += (i-j) * 1
    if ans1+bag >= ans2 and time <= total:
        total = time
        totalnum = i

print(total, totalnum)