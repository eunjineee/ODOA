import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

q= deque([])
for _ in range(n):
    a = list(input().split())
    if a[0] == 'push':
        q.append(a[1])
    elif a[0] == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)