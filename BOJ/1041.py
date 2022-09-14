n = int(input())
li = list(map(int, input().split()))
lili = [[1,2],[2,4],[1,3],[3,4]]
sumli = []
for i in [0,5]:
    for j in lili:
        all = [li[i],li[j[0]],li[j[1]]]
        sumli.append(sum(all))
soso = min(li)                             #가장 작은 숫자
maju = [5,4,3,2,1,0]                       #인덱스당 마주보는 면의 인덱스 주머니
dodoban = maju[li.index(soso)]             #소소의 반대면 인덱스
mini = 51                                  #주사위 숫자의 최대값 50
for k in range(6):
    if k == dodoban or k == li.index(soso):
        continue
    else:
        if li[k] < mini:
            mini = li[k]
           
if n == 1:
    li.sort()
    print(sum(li[0:5]))                     #주사위의 바닥면 제외하고 더하기
else:
    total = min(sumli) * 4 + (soso+mini)* ((n-2)*8+4) + soso * ((n-2)*(n-2)*5+(n-2)*4) #n이 2일때, 4,0 남기기
    print(total)