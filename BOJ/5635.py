n = int(input())

ans = ''
answer = 20110000
topans = ''
topanswer = 19890000
for _ in range(n):
    name, dd, mm, yyyy = input().split()
    if int(dd) < 10:
        dd = '0' + dd
    if int(mm) < 10:
        mm = '0' + mm
    day = yyyy + mm + dd
    if int(day) < answer:
        answer = int(day)
        ans = name
    if int(day) > topanswer:
        topanswer = int(day)
        topans = name

print(topans)
print(ans)

