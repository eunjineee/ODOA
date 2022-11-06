num = input()
if len(num) == 1:
    num = '0' + num
number = num
ans = 0
while True:
    a, b = number
    ab = int(a) + int(b)
    if ab >= 10:
        n, ab = str(ab)
    number = b + str(ab)
    ans += 1
    if num == number:
        break
print(ans)
