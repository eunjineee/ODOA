import sys
input = sys.stdin.readline

def powerset(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        bit[i] = 0
        powerset(i+1, k)
        bit[i] = 1
        powerset(i+1, k)


n, m = map(int,input().split())
p = [0] * m
used = [0] *n
arr = [x for x in range(1, n+1)]
f(0,n)