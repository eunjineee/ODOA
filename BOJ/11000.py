n = input()

if n[0] == '1':
    a = 1 + n.count('01')
    b = n.count('10')
else:
    a = n.count('01')
    b = 1 + n.count('10')


if a > b:
    print(b)
else:
    print(a)
