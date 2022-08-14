a, b= map(int,input().split())
nums = list(map(int, input().split()))
num = []

for i in nums:
    if i < b :
        num.append(i)

print(*num)