n, m = int(input().split())
target = list(map(int, input().split()))
nums = [x for x in range(n)]

while len(target) == 0:
    