n, m = map(int, input().split())
gift = list(map(int, input().split()))
children = list(map(int, input().split()))

gift.sort()
children.sort()
if m <= n:
    for i in range(1, m+1):
        if gift[-i] >= children[-i]:
            continue
        else:
            print(0)
            exit()
    print(1)
else:
    print(0)
