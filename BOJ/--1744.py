n = int(input())

nums =[]
ans = 0
for i in range(n):
    a = int(input())
    if a <= 1:
    elif a <
        numzero.append(a)
    else:
        nums.append(a)

nums.sort(reverse=True)

if len(nums) >= 2:
    if len(nums) % 2 == 1:
        ans += nums[-1]
        number = len(nums)//2
    else:
        number = len(nums)//2
    # print(f'number={number}')
    for j in range(number):
        ans += nums[j*2] * nums[j*2+1]
        # print(nums[j*2] , nums[j*2+1])

if 

print(ans)