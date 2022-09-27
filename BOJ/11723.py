import sys
input = sys.stdin.readline
sys.stdin = open('input.txt')

m = int(input())

s = []
for _ in range(m):
    a = list(input().split())
    if a[0] == 'add':
        if a[1] not in s:
            s.append(a[1])
    elif a[0] == 'check':
        if a[1] in s:
            print(1)
        else:
            print(0)
    elif a[0] == 'remove':
        if a[1] in s:
            s.remove(a[1])
    elif a[0] == 'toggle':
        if a[1] in s:
            s.remove(a[1])
        else:
            s.append(a[1])
    elif a[0] == 'all':
        s = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    elif a[0] == 'empty':
        s = []