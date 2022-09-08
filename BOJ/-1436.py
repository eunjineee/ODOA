n = int(input())
a = 666

b = (n-13) % 24
c = n % 24
if 13 >= c >= 7:
    num = b*1000 + a
elif 