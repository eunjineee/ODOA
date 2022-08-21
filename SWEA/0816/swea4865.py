T = int(input())

for t in range(1,T+1):
    a = input()
    b = input()
    a = set(a)
    bbli = []
    for i in a:
        bb = b.count(i)
        bbli.append(bb)
    print(f'#{t} {max(bbli)}')