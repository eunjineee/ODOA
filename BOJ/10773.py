N = int(input())
nums = []
for n in range(N):
    num = int(input())
    if num != 0:
        nums.append(num)
    else:
        nums.pop()
print(sum(nums))