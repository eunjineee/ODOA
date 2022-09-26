import sys
sys.stdin = open('input.txt')


    from collections import deque

T = int(input())


for t in range(T):
    n, m = map(int, input().split())
    nums = deque(map(int, input().split()))
    a = deque('0'*n)
    a[m] = '1'
    ans = 0

    while '1' in a:
        if nums[0] != max(nums):
            nums.rotate(-1)
            a.rotate(-1)
        else:
            nums.popleft()
            a.popleft()
            ans += 1

    print(ans)