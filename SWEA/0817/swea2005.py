T = int(input())

for t in range(T):
    n = int(input())
    nums=[[1] for _ in range(n)] #여기에 스파이가 있다 !!! 두둥!!!탁!!!

    for i in range(1,n):
        for j in range(i-1):
            nums[i].append(nums[i-1][j]+nums[i-1][j+1])
        nums[i].append(1)

    print(f'#{t+1}')
    for j in nums:
        for i in j:
            print(i,end=' ')
        print()