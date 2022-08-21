n, c = map(int,input().split())
gil = []
for _ in range(n):
    gil.append(int(input()))
gil.sort()
while num != c:
    mid = (st + ed) // 2
    if gil[mid]  