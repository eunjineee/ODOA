import sys
sys.stdin = open('swea4843.txt')

T = int(input())

for t in range(1, T+1):
    num = int(input())
    nums = list(map(int, input().split()))
    for i in range(num-1):
        for j in range(i+1,num):
            if i % 2 == 0:
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
    print(f'#{t}',end=' ')
    for x in range(10):
        print(nums[x],end=' ')
    print()