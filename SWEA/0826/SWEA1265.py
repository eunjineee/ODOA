T = int(input())

for t in range(T):
    n, p =map(int, input().split())
    if n % p == 0:
        ans = (n//p)**p
    else:
        namugi = n % p 
        mock = n // p
        ans = mock**(p - namugi) * (mock + 1)**namugi
    print(f'#{t+1} {ans}')