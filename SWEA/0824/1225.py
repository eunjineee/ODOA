import sys
sys.stdin = open('1225.txt')

from collections import deque

for _ in range(10):
    t = int(input())
    nums = deque(map(int, input().split()))
    a = [1,2,3,4,5]
    j = 0
    while True:
        nums[0] -= a[j % 5]
        j += 1
        nums.rotate(-1)
        if nums[-1] <= 0:
            nums[-1] = 0
            break
    print(f'#{t}',end=' ')
    for h in nums:
        print(h,end=' ')
    print()