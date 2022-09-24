import sys
sys.stdin = open('input.txt')

n, m, bag = map(int, input().split())

ground = []

for _ in range(n):
    ground += list(map(int, input().split()))
ground.sort()

subbag1 = subbag2 = 0
middle = round(sum(ground) // (n*m))
for i in ground:
    if middle > i:
        subbag1 += (middle - i)
    elif i > middle:
        subbag2 += i - middle

ans = 0
while ground[0] != ground[-1]:
    if subbag2 <= subbag1*2:
        ground.append(ground.pop(0)+1)
        bag -= 1
        ground.sort()
        ans += 1
    else:
        ground.append(ground.pop()-1)
        bag -= 1
        ground.sort()
        ans += 2
print(ans,ground[0])