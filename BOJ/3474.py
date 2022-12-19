import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    a = int(input())
    ans = 0
    b = 5
    while b <= a:
        ans += a // b
        b *= 5
    print(ans)