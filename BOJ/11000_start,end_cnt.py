'''
3
1 3
2 4
3 5
'''

import sys
input = sys.stdin.readline
n = int(input())

nums = []
for _ in range(n):
    start, end = map(int, input().split())
    nums.append((start, 1))
    nums.append((end, 0))
nums.sort()
#print(nums)  >> [(1, 1), (2, 1), (3, 0), (3, 1), (4, 0), (5, 0)]

total = [0] * n*2
for i in range(0, n*2):
    if nums[i][1] == 1:
        total[i] = total[i-1] + 1
    else:
        total[i] = total[i-1] - 1
#print(total) >>[1, 2, 1, 2, 1, 0]

print(max(total))
