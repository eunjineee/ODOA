import sys
import heapq
input = sys.stdin.readline
n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]

nums.sort()
total = []
heapq.heappush(total, nums[0][1])

for i in range(1,n):
    end = total[0]
    if nums[i][0] >= end:
        heapq.heappop(total)
        heapq.heappush(total, nums[i][1])      
    else:
        heapq.heappush(total, nums[i][1])      

print(len(total))