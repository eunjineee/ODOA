n = int(input())
nums = list(map(int, input().split()))
small = 1
big = 1
li = []

for i in range(1,n):
    if nums[i-1] < nums[i]:
        big += 1
        li.append(small)
        small = 1
    elif nums[i-1] > nums[i]:
        small += 1
        li.append(big)
        big = 1
    else:
        small += 1
        big += 1
li.append(small)
li.append(big)

print(max(li))