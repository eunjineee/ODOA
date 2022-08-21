from collections import deque
from operator import index
n, m = map(int, input().split())
target = deque(map(int, input().split()))
nums = deque(x for x in range(1,n+1))
cnt = 0

while len(target) != 0:
    if nums[0] == target[0]:
        target.popleft()
        nums.popleft()

    elif nums.index(target[0]) > len(nums)//2 :
        cnt += len(nums)-nums.index(target[0])
        nums.rotate(len(nums)-nums.index(target[0]))
    else:
        cnt += nums.index(target[0])
        nums.rotate(-nums.index(target[0]))

print(cnt)