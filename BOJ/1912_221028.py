n =int(input())
nums = list(map(int, input().split()))
visited = [nums[0]]
for i in range(n-1):
    visited.append(max(visited[i]+nums[i+1], nums[i+1]))
    
print(max(visited))