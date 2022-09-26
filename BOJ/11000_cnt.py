import sys
input = sys.stdin.readline
n = int(input())

nums = []
for _ in range(n):
    start, end = map(int, input().split())
    nums.append((start, 1))
    nums.append((end, 0))
nums.sort()

max_count = 0
count = 0
for i in range(0, n*2):
    if nums[i][1] == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count -= 1
    
print(max_count)