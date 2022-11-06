n = int(input())

for i in range(n):
    print(' '*i + '*'*(n-i) + '*'*(n-i-1))