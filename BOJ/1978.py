n = int(input())
nums = list(map(int, input().split()))
to = []
if 1 in nums:
    nums.remove(1)
for i in nums:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        to.append(i)
print(len(to))