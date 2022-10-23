n = int(input())

for i in range(n):
    nums = []
    a, b = map(int, input().split())
    for j in range(1,5):
        nums.append(a**j)    
    c = b % 4
    ans = nums[c-1]%10
    if ans == 0:
        ans = 10
    print(ans)