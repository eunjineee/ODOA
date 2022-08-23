from collections import deque

N = int(input())
note1 = deque(map(int,input().split()))
M = int(input())
note2 = deque(map(int, input().split()))
total = [0] * M
for i in note1:
    for j in range(M):
        if i == note2[j]:
            total[j] += 1

print(*total)
            
