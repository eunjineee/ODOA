a,b = map(int,input().split())
c = int(input())

total = a * 60 + b + c

if total >= 60 * 24:
    total = total - 60*24

h = total//60
m = total%60

print(f'{h} {m}')