from collections import deque
a, b = map(int, input().split())
nums = deque()
to = []
for i in range(1, a+1):
    nums.append(i)

while True:
    if len(nums) == 0:
        False
        break
    nums.rotate(-b)
    to.append(nums.pop())

print("<", end = '')
print(*to,sep=", ",end="")
print('>')
