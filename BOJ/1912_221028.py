n =int(input())
nums = list(map(int, input().split()))
visited = [-1000]*n
for i in range(1,n):
    visited[i] = max(nums[i-1]+nums[i], nums[i])
    
print(max(visited))