import sys
input = sys.stdin.readline
t = int(input())

nums =[]
numbers = {}
for T in range(t):
    a = int(input())
    nums.append(a)
    if a in numbers.keys():
        numbers[a] += 1
    else:
        numbers[a] = 1
nums.sort()

ans1 = round(sum(nums)/t) 
ans2 = nums[t//2]

ans3li=[]
for i,j in numbers.items():
    if j == max(numbers.values()):
        ans3li.append(i)
if len(ans3li) < 2:
    ans3 = ans3li[0]
else:
    ans3li.sort()
    ans3 = ans3li[1]

ans4 = nums[-1] - nums[0]

print(ans1)
print(ans2)
print(ans3)
print(ans4)