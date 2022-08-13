import sys

T = int(input())
nums=[]
for t in range(T):
    a, b = map(int, sys.stdin.readline().split())
    nums.append((a, b))
    
nums.sort()

for i in nums:
    print(f'{i[0]} {i[1]}')