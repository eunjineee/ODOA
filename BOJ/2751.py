import sys

T = int(input())
nums = []
for t in range(T):
    a = int(sys.stdin.readline())
    nums.append(a)
    
nums.sort()

for i in nums:
    print(f'{i}')