import sys
N = int(input())

<<<<<<< HEAD
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
=======
count = [0] * (10000 + 1)

for num in range(N):
    mm = int(sys.stdin.readline())
    count[mm] += 1 

for n in range(10001):
    if count[n] != 0:
        for i in range(count[n]):
            print(n)
>>>>>>> d22c68645c14fb6e3fad69d51cf6a73441966d9c
