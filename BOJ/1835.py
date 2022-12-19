from collections import deque

n = int(input())
num = deque([n])

for j in range(n-1,0,-1):
    num.appendleft(j)
    for k in range(j):
        num.rotate(1)

print(*num)
