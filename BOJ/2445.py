n = int(input())

for i in range(1,n+1):
    ans = '*'*i + ' '*(n-i)*2 + '*'*i
    print(ans)

for j in range(n-1, 0, -1):
    ans = '*'*j + ' '*(n-j)*2 + '*'*j 
    print(ans)