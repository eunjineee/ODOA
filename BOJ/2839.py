a = int(input())
num = 0
if a % 5 == 0 :
    print(a//5)
while a % 5 != 0:
    if a < 0:
        print(-1)
        break
    a = a - 3
    num += 1
    if a % 5 == 0:
        num += a // 5 
        print(num)
