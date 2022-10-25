nums = []
treedic = {}
while True:
    try:
        a = int(input())
        nums.append(a)
        treedic[a] = [-1,-1]
    except ValueError:
        break
i = 1
for ii in range(1, len(nums)):
    while True:
        if nums[ii] < nums[i-1]:
            if treedic[nums[i-1]][0] == -1:
                treedic[nums[i-1]][0]=nums[ii]  
                i += 1
                break
            else:
                i -= 1
        elif nums[ii] > nums[i-1]:
            if treedic[nums[i-1]][1] == -1:
                treedic[nums[i-1]][1] = nums[ii]  
                i += 1
                break
            else:
                i -= 1
            
            
print(treedic)