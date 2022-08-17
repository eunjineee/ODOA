nums = [i for i in range(1, 31)]
for j in range(28):
    n = int(input())
    nums.remove(n)

for x in nums:
    print(x)