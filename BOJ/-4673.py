totalnum = set(range(1,10001))
nums = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    nums.add(i)

self_nums = sorted(totalnum-nums)
for k in self_nums:
    print(k)
