a = int(input())
b = list(map(int, input().split()))
total = 0
mb = max(b)

for i in b:
    if i < mb:
        total += ( i / mb * 100)
    else:
        total += ( i / mb * 100)

print(total/a)
        