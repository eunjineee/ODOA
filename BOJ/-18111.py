n,m,b = map(int, input().split())

nums = []
totala = 0
for _ in range(n):
    a = list(map(int, input().split()))
    nums += a
    totala += sum(a)

while totala//(n*m) != nums[-1]:
    