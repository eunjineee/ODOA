n = int(input())
a = 665
cnt = 0
while cnt != n:
    a += 1
    if '666' in str(a):
        cnt += 1
    
print(a)

#ㅇ어려운거 아님,.
# a = 666

# b = (n-13) // 24 + 1
# c = n % 24
# print(b,c)

# if 6 >= c >= 0:
#     num = b*10000 + (c-1)*1000 + a
# elif 13 >= c >= 7:
#     num = b*10000 + a*10 + (c-7)
# elif 23 >= c >= 14:
#     num = (b-2)*10000 + (c-13)*1000 + a

# print(num)