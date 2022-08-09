import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    to = 0
    top = mini = nums[0]
    for j in nums:
        if top < j:
            top = j
        if mini > j:
            mini = j
    to = top - mini
    print(f'#{i} {to}')