import sys

T = int(input())
nums=[]
for t in range(T):
    a, b = map(int, sys.stdin.readline().split())
    nums.append((a, b))
nums.sort(key=lambda x:x[0])
nums.sort(key=lambda y:y[1])
for i in nums:
    print(f'{i[0]} {i[1]}')