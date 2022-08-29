while True:
    nums = list(map(int,input().split()))
    nums.sort()
    if nums == [0,0,0]:
        break
    if nums[2] < nums[0] + nums[1]:
        if nums[2]**2 == nums[0]**2 + nums[1]**2:
            print('right')
        else:
            print('wrong')
    else:
        print('wrong')