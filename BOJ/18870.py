n = int(input())
nums = list(map(int, input().split()))
number = list(set(nums))
number.sort()
di = {}
for i in range(len(number)):
    di[number[i]] = i

for j in nums:
    print(di[j],end=' ')