nums = [int(input()) for x in range(10)]
nu = []
for i in range(10):
    nu.append(nums[i]%42)

n = len(set(nu))

print(n)