import sys
n= int(input())
num1 = list(map(int,sys.stdin.readline().split()))
num2 = list(map(int,sys.stdin.readline().split()))
number={}
for i in range(len(num2)):
    sun = 0
    for j in range(len(num2)):
        if num2[i] > num2[j]:
            sun += 1
    val = number.keys()
    if sun in val:
        number[sun+1] = num2[i]
    else:
        number[sun] = num2[i]
print(number)
num = sorted(num1)
print(num)
total = 0

for x in range(n):
    total += number[x] * num[n-1-x]

print(total)