from collections import deque
import sys
input = sys.stdin.readline
r, c = map(int, input().split())
al = [list(input().strip())for _ in range(r)]
q = deque()
total = []

def f(x, y):
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    q.append((x,y))
    while q :
        x, y = q.pop()
        for dd in d:
            nx = x + dd[0]
            ny = y + dd[1]
            if 0 <= nx < c and 0 <= ny < r:
                if al[ny][nx] not in total:
                    total.append(al[ny][nx])
                    q.append((nx, ny))
        total.pop()

f(0,0)
print(len(total))