import math
num = {}
for i in range(10):
    num[i] = 0

n = list(map(int,list(input())))

for j in n:
    num[j] += 1
    
num[6] = math.ceil((num[6] + num[9])/2)
num[9] = 0 

total = max(num.values())

print(total)