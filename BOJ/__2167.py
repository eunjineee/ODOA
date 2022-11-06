import sys
input = sys.stdin.readline

n,m = map(int, input().split())

nums = []
numbers = [[0]*(m+1) for _ in range(n)]

for i in range(n):
    nums = [0] + list(map(int, input().split()))
    for ii in range(1,m+1):
        try:
            print(f'1 : {numbers[i][ii-1]} + {nums[ii]}')
            numbers[i][ii] = numbers[i][ii-1] + nums[ii]
        except:
            continue

print(numbers)

t = int(input().rstrip())
for _ in range(t):
    i,j,x,y = map(int, input().split())
    total = 0
    for ii in range(i-1, x):
        total += numbers[ii][y-1] - numbers[ii][j-1]
        print(f'total: {total} = {numbers[ii][y-1]} - {numbers[ii][j-1]}')

    print(total)