import heapq
k, n = map(int,input().split())
nums = heapq()

for _ in range(k):
    nums.heapqushint(input()))

numbers = nums[:]

while len(nums) < n:
    a = nums.leftpop()[1]//2
    b = 0
    for j in numbers:
        b += j//a
    if b >= n:
        print(a)
        break
    nums.heapqush(nums, (-a,a))
    