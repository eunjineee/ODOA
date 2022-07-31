a, b = list(map(int, input().split()))


c = a * 60 + b - 45

if c > 0:
    h = c // 60
    m = c % 60
else:
    c = 60 * 24 + c
    h = c // 60
    m = c % 60

if h > 24:
    h = h - 24
elif h == 24:
    h = 0

print(f'{h} {m}')