from collections import deque
import sys
n = int(input())
nums = deque()

for _ in range(n):
    a = list(sys.stdin.readline().split())
    
    if a[0] =='push':
        nums.append(a[1])
    elif a[0] == 'pop':
        if len(nums) ==0 :
            print(-1)
        else:
            print(nums.popleft())
    elif a[0] == 'size':
        print(len(nums))
    elif a[0] == 'empty':
        if len(nums) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(nums) ==0 :
            print(-1)
        else:
            print(nums[0])
    elif a[0] == 'back':
        if len(nums) ==0 :
            print(-1)
        else:
            print(nums[-1])           