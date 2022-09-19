k, n = map(int,input().split())
nums = []
for _ in range(k):
    nums.append(int(input()))

start = 1
end = max(nums)

while start <= end:
    mid = (start + end)//2
    b = 0
    # print(f'{start} {mid} {end}')
    for j in nums:
        b += j//mid
    if b >= n:
        start = mid + 1
        # print(f'커{b} {start} {mid} {end}')
    else:
        end = mid - 1
        # print(f'작아{b} {start} {mid} {end}')
print(end)

# print(f'{start} {number} {mid}')

'''
k, n = map(int,input().split())
nums = []
for _ in range(k):
    nums.append(int(input()))
numbers = nums[:]
nums.sort()

while len(nums) < n:
    a = nums.pop()//2
    b = 0
    for j in numbers:
        b += j//a
    if b >= n:
        print(a)
        break
    nums.append(a)
    nums.sort()
    '''
