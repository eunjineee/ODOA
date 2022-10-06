import sys
input = sys.stdin.readline

def f(i,k):
    if i == m:
        pp = p[:]
        # for q in range(len(pp)-1):
        #     if pp[q] > pp[q+1]:
        #         break
        # else:
        pp.sort()
        total.append(pp)
    else:
        for j in range(k):
            p[i] = arr[j]    
            f(i+1, k)    


n, m = map(int,input().split())
p = [0] * m
arr = [x for x in range(1, n+1)]
total = []
f(0,n)
total.sort()
print(*total[0])
for to in range(1,len(total)):
    if total[to] != total[to-1]:
        print(*total[to])