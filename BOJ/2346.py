from collections import deque

n = int(input())
nums = list(map(int, input().split()))
numbers = deque([])
for j in range(1,n+1):
    numbers.append((j,nums[j-1]))

ans =[]
while numbers: 
    num0, num1 = numbers.popleft()
    ans.append(num0)
    if num1 > 0 :
        num1 -= 1
    numbers.rotate(-num1)

print(*ans)