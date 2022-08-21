T = int(input())
for t in range(1,T+1):
    a, b = input().split()
    a = a.replace(b,' ')
    print(f'#{t} {len(a)}')

'''
3
banana bana
asakusa sa
hellolll ll
'''