def comb(n, r):
    if r == 0:
        st = ''
        numj = 0
        numm = 0
        p2 = p[:]
        p2.sort()
        for pp in p2:
            st += pp
            if pp in mo:
                numm += 1
            else:
                numj += 1
        if numm > 0 and numj > 1:
            total.append(st)
    elif n < r:
        return
    else:
        p[r-1] = al[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

l, c = map(int, input().split())
al = list(input().split(' '))

mo = ['a','e','i','o','u']

total = []
p = [0] * l
comb(c, l)

total.sort()
for to in total:
    print(to)