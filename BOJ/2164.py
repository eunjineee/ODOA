from collections import deque
n = int(input())
nums = deque()

for i in range(1,n+1):
    nums.append(i)

while True:
    if len(nums) == 1:
        False
        break
    nums.popleft()
    nums.rotate(-1)
print(nums[0])