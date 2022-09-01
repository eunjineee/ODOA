import sys
N = int(input())

count = [0] * (10000 + 1)

for num in range(N):
    mm = int(sys.stdin.readline())
    count[mm] += 1 

for n in range(10001):
    if count[n] != 0:
        for i in range(count[n]):
            print(n)
