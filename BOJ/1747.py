import math
n = int(input())

def sosu(b):
    for i in range(2, int(math.sqrt(b))+1):
        if b % i == 0 :
            return 0            
    return 1

if n == 1:
    print(2)
    exit()

while True:
    if str(n) == str(n)[::-1]:
        if sosu(n):
            print(n)
            break
    n += 1
