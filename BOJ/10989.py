import sys
N = int(sys.stdin.readline().rstrip())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

count = [0] * (max(arr) + 1)

for num in arr:
    count[num] += 1
    
for i in range(1, len(count)):
    count[i] += count[i-1]

result = [0] * (len(arr))

for num in arr:
    idx = count[num]
    result[idx - 1] = num
    count[num] -= 1

for i in result:
    print(i)
