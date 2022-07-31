a = list(input().split(' '))

for i in range(2):
    if '' in a:
        a.remove('')

print(len(a))
